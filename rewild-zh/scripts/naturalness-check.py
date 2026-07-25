#!/usr/bin/env python3
"""Naturalness check: statistical AI-tell screening for EN / ZH / DE text.

Usage:
    python3 naturalness-check.py FILE [--source ORIGINAL] [--lang en|zh|de]
    python3 naturalness-check.py --audit [--lang en|zh|de]

Screens a text for the measurable signals described in the Rewild pattern
catalogs: sentence-length uniformity, repeated sentence openers, uniform
paragraph sizes, AI vocabulary, and punctuation problems. Zero dependencies.

--source turns on the fidelity pass, which is the more important half. Style
tells are what the model is already good at removing; fidelity is where
rewrites actually break. It compares the rewrite against the original and
flags four things, each an observed failure mode rather than a theoretical
one:

  * names, numbers and dates in the rewrite that are not in the original
  * attributed claims ("observers have cited X") that became bare assertions
  * commitments ("we'll send an update") the original never made
  * severity raised beyond what the original said

A style warning is a suggestion. A fidelity warning is a defect: the rewrite
is now saying something the source did not.

Exit status is 0 when the report is clean and 1 when anything is flagged, so
the check can gate a workflow. It measures signals, not truth — a clean report
does not prove the text reads well. Judgment stays with the writer.

--audit compares the word lists below against `references/patterns.md` and
reports terms the catalog documents but the checker cannot see. Run it after
editing a catalog so the two never drift apart.
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

# Terms that raise a warning. Kept in sync with the "AI vocabulary" pattern in
# each catalog; matched with light inflection (showcase → showcasing/showcased).
AI_WORDS_EN = [
    "additionally", "moreover", "furthermore", "boast", "breathtaking",
    "comprehensive", "crucial", "cutting-edge", "delve", "elevate", "embark",
    "enduring", "enhance", "exemplify", "foster", "game-changing", "garner",
    "groundbreaking", "holistic", "interplay", "intricacy", "intricate",
    "intuitive", "leverage", "myriad", "nestle", "pivotal", "realm",
    "renowned", "robust", "seamless", "showcase", "streamline", "stunning",
    "tapestry", "testament", "underscore", "vibrant",
]
AI_PHRASES_EN = [
    # hedged notes and closers
    "it's worth noting", "it is worth noting", "it's important to note",
    "it is important to note", "in conclusion", "in summary", "to sum up",
    "not only", "plays a crucial role", "stands as", "serves as",
    "ever-evolving", "indelible mark", "reflects broader", "must-visit",
    "everything from",
    "underscores its importance", "highlights its importance",
    "several sources", "several publications",
    # formulaic openers
    "in today's", "fast-paced world", "in an era where",
    "have you ever wondered", "imagine a world where", "picture this",
    "since the dawn of", "throughout history", "in recent years,",
    # empty future framing
    "sets the stage", "setting the stage for", "marks a shift",
    "future looks bright", "exciting times lie ahead", "looking ahead",
    "only time will tell", "it remains to be seen",
    "journey toward excellence", "the biggest lesson i learned",
    "this experience taught me",
    # vague attribution
    "industry reports", "observers have cited", "experts argue",
    "experts believe", "some critics argue", "commitment to",
    # outline skeletons
    "despite these challenges", "challenges and legacy", "future outlook",
    # assistant artifacts
    "let me break this down", "let me walk you through", "here's the thing",
    "the real question is", "what most people get wrong",
    "here's what nobody tells you", "the part everyone misses",
    "what if i told you", "the short answer is", "so here's what happened",
    "what struck me most", "i find it fascinating that", "i hope this helps",
    "you're absolutely right", "would you like me", "certainly!",
    "of course!", "while specific details are limited",
    "up to my last training update",
]
# Context-dependent terms: reported for visibility, never flagged. "landscape"
# is AI slop in "the evolving landscape" and plain English in a gardening post.
AI_WATCH_EN = [
    "align", "collaboration", "contributing", "emphasizing", "ensuring",
    "establishment", "examination", "facilitation", "highlight",
    "implementation", "journey", "key", "landscape", "navigate",
    "optimization", "powerful", "profound", "reflecting", "rich",
    "symbolizing", "transformation", "ultimately", "unlock", "utilization",
    "valuable",
]

AI_WORDS_DE = [
    "zudem", "folglich", "nichtsdestotrotz", "zusammenfassend",
    "abschließend", "infolgedessen", "innovativ", "nahtlos", "ganzheitlich",
    "bahnbrechend", "facettenreich", "maßgeblich", "essenziell",
    "meilenstein", "umfassend", "eintauch", "unterstreich", "vielfältig",
    "atemberaubend", "renommiert", "tiefgreifend", "zusätzlich",
]
AI_PHRASES_DE = [
    "darüber hinaus", "in der heutigen zeit", "im digitalen zeitalter",
    "es ist wichtig zu beachten", "tauchen wir ein", "eine vielzahl",
    "breite palette", "nicht nur", "schlüsselrolle", "lässt sich sagen",
    "auf ein neues level", "es lässt sich nicht leugnen", "seit jeher",
    "in einer welt, in der", "bleibt festzuhalten", "insgesamt zeigt sich",
    "es bleibt spannend", "die zukunft wird zeigen",
    "was die meisten übersehen", "die eigentliche frage ist",
    "lassen sie uns eintauchen", "hier ist eine aufschlüsselung",
    "das sagt dir niemand", "was die meisten falsch machen",
    "immer mehr menschen fragen sich", "fazit:", "dient als",
    "steht für", "eingebettet in", "spiegelt breitere trends wider",
    "ist ein beweis", "ist ein zeugnis", "bis hin zu", "angefangen bei",
]
AI_WATCH_DE = [
    "effizient", "entscheidend", "ermöglich", "landschaft", "lebendig",
    "markiert", "präzise", "spannend", "zentral",
]

AI_PHRASES_ZH = [
    "此外", "值得注意的是", "值得一提的是", "综上所述", "总而言之",
    "总的来说", "与此同时", "不难发现", "在当今", "众所周知", "赋能",
    "砥砺前行", "不忘初心", "深耕细作", "精益求精", "高质量发展",
    "开拓创新", "与时俱进", "未来可期", "我们有理由相信", "深刻变革",
    "不可忽视", "近年来，随着", "随着人工智能", "展望未来", "守正创新",
    "行稳致远", "新质生产力", "数字化转型", "机遇与挑战并存",
    "在此基础上", "特别需要关注的是", "需要指出的是", "必须强调的是",
    "基于以上分析", "具体来说", "另一方面", "在一定程度上", "某种程度上",
    "起到了积极作用", "首先，", "其次，", "最后，", "相信在不久的将来",
    "很多人都忽略了", "没人告诉你的是", "大多数人都搞错了",
    "真正的问题其实是", "让我来分析", "下面我将", "进行优化", "开展实施",
    "随着科技的发展", "无缝", "彰显", "构成了",
]
AI_WATCH_ZH = [
    "显著", "构建", "机制", "框架", "促进", "体现", "有助于", "提升",
    "随着", "然而", "不仅",
]

ZH_PARTICLES = "呢啊吧嘛哦啦哇喽呀"
DE_MODAL_PARTICLES = [
    "doch", "halt", "mal", "eben", "ja", "schon", "wohl", "eigentlich",
    "übrigens",
]

# Titles are always followed by a name, so their period never ends a sentence.
ABBREV_TITLE = {
    "en": ["mr", "mrs", "ms", "dr", "prof", "rev", "hon", "sr", "jr", "st",
           "fig", "vol", "no", "dept", "approx"],
    "de": ["dr", "prof", "hr", "fr", "st", "nr", "abb", "bd", "ca"],
}
# These can also close a sentence ("...at 4 p.m. The team left"), so their
# period is only hidden when the next word is not capitalized.
ABBREV_OTHER = {
    "en": ["vs", "etc", "e.g", "i.e", "cf", "al", "inc", "ltd", "co", "corp",
           "est", "min", "max", "a.m", "p.m", "ph.d", "jan", "feb", "mar",
           "apr", "jun", "jul", "aug", "sep", "sept", "oct", "nov", "dec",
           "mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    "de": ["z.b", "u.a", "d.h", "bzw", "evtl", "ggf", "inkl", "exkl", "vgl",
           "usw", "etc", "mio", "mrd", "jh", "bspw", "allg", "engl", "dt",
           "s.o", "s.u", "o.g", "jan", "feb", "mär", "apr", "jun", "jul",
           "aug", "sep", "okt", "nov", "dez"],
}

DOT = "\x00"  # stand-in for a period that does not end a sentence
CJK = r"㐀-䶿一-鿿豈-﫿"
WORD_RE = re.compile(
    r"[0-9A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+(?:['’\-][0-9A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+)*")
CJK_RE = re.compile(f"[{CJK}]")

sections = []
flags = []


def section(title):
    sections.append({"title": title, "lines": []})
    print(f"\n{title}")


def report(ok, message):
    if not ok:
        flags.append({"section": sections[-1]["title"] if sections else "",
                      "message": message})
    if sections:
        sections[-1]["lines"].append({"ok": ok, "message": message})
    print(f"{'  ·' if ok else '  ⚠'} {message}")


def note(message):
    if sections:
        sections[-1]["lines"].append({"ok": True, "message": message})
    print(f"  · {message}")


def is_cjk(ch):
    return bool(CJK_RE.match(ch))


def fold(text):
    """Normalize typography so matching is not defeated by smart quotes."""
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"')
                .replace("‑", "-").replace(" ", " ").lower())


def strip_markdown(text):
    """Drop markdown scaffolding that is not prose, keep the prose."""
    stats = {"code": 0, "heading": 0, "table": 0}
    text, stats["code"] = re.subn(
        r"(?ms)^[ \t]*(?:```|~~~).*?^[ \t]*(?:```|~~~)[ \t]*$", "", text)
    text = re.sub(r"(?s)<!--.*?-->", "", text)

    kept = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("|"):
            stats["table"] += 1
            continue
        if re.match(r"^#{1,6}\s", stripped):
            stats["heading"] += 1
            kept.append("")  # a heading is a break, not a sentence
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            continue
        kept.append(line)
    text = "\n".join(kept)

    text = re.sub(r"(?m)^[ \t]*>+[ \t]?", "", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)

    # A list item is its own sentence; give it a terminator so it does not
    # merge with the line below and distort every length statistic.
    out = []
    for line in text.split("\n"):
        m = re.match(r"^([ \t]*)(?:[-*+]|\d+[.)])[ \t]+(.*)$", line)
        if m:
            body = m.group(2).rstrip()
            if body and body[-1] not in ".!?:;。！？…":
                body += "。" if CJK_RE.search(body) else "."
            out.append(body)
        else:
            out.append(line)
    return "\n".join(out), stats


def detect_lang(text):
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return "en"
    cjk = sum(1 for c in letters if is_cjk(c))
    if cjk / len(letters) > 0.2:
        return "zh"
    de_hits = len(re.findall(
        r"\b(der|die|das|und|nicht|ist|ein|eine|mit|für|auf|werden|wird)\b",
        text.lower()))
    en_hits = len(re.findall(
        r"\b(the|and|of|to|is|that|for|with|was|are|this|not)\b",
        text.lower()))
    return "de" if de_hits > en_hits else "en"


def split_paragraphs(text):
    paras = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paras if p.strip()]


def protect_periods(text, lang):
    """Hide periods that belong to abbreviations, decimals, and initials."""
    hide = lambda m: m.group(0).replace(".", DOT)  # noqa: E731
    for abbr in ABBREV_TITLE.get(lang, []):
        text = re.sub(rf"(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ]){re.escape(abbr)}\.",
                      hide, text, flags=re.I)
    for abbr in ABBREV_OTHER.get(lang, []):
        text = re.sub(
            rf"(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ]){re.escape(abbr)}\.(?!\s+[A-ZÄÖÜ])",
            hide, text, flags=re.I)
    text = re.sub(r"(?<=\d)\.(?=\d)", DOT, text)
    text = re.sub(r"(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ])([A-ZÄÖÜ])\.", rf"\1{DOT}", text)
    return text


def split_sentences(text, lang):
    if lang == "zh":
        parts = re.split(r"[。！？…]+", text)
    else:
        protected = protect_periods(text, lang)
        parts = re.split(r"(?<=[.!?…])[\"'”’)\]]*\s+", protected)
        parts = [p.replace(DOT, ".") for p in parts]
    return [s.strip() for s in parts if s.strip()]


def sentence_length(sentence, lang):
    if lang == "zh":
        # Count Han characters plus each run of Latin/digits as one unit, so
        # mixed-script technical Chinese is not systematically undercounted.
        cjk = len(CJK_RE.findall(sentence))
        latin = len(WORD_RE.findall(re.sub(f"[{CJK}]", " ", sentence)))
        return cjk + latin
    return len(WORD_RE.findall(sentence))


def inflections(word, lang):
    """Regex alternatives for the ordinary English/German inflections."""
    if " " in word or "-" in word:
        return re.escape(word)
    stem = re.escape(word)
    if lang == "de":
        # Covers adjective declension (innovative/-en/-er/-es) and the common
        # verb endings, which is why some entries are stems (unterstreich).
        return stem + r"(?:e|en|em|er|es|n|s|t|te|ten|end)?"
    if word.endswith("e"):
        return re.escape(word[:-1]) + r"(?:e|es|ed|ing)"
    if word.endswith("y") and len(word) > 2 and word[-2] not in "aeiou":
        return re.escape(word[:-1]) + r"(?:y|ies|ied|ying)"
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return stem + r"(?:es|ed|ing)?"
    return stem + r"(?:s|ed|ing)?"


def count_hits(text, words, phrases, lang):
    hits = {}
    for word in words:
        if lang == "zh":
            n = text.count(word)
            if n:
                hits[word] = hits.get(word, 0) + n
            continue
        for found in re.findall(rf"\b{inflections(word, lang)}\b", text):
            hits[found] = hits.get(found, 0) + 1
    for phrase in phrases:
        n = text.count(phrase)
        if n:
            hits[phrase] = hits.get(phrase, 0) + n
    return sorted(hits.items(), key=lambda x: (-x[1], x[0]))


def check_rhythm(sentences, lang):
    section("Rhythm")
    lengths = [sentence_length(s, lang) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 4:
        note("too few sentences for rhythm statistics")
        return
    mean = statistics.mean(lengths)
    stdev = statistics.pstdev(lengths)
    # Judge the printed value, so the verdict never contradicts the number.
    cv = round(stdev / mean, 2) if mean else 0
    unit = "chars" if lang == "zh" else "words"
    note(f"{len(lengths)} sentences, mean {mean:.1f} {unit}, "
         f"min {min(lengths)}, max {max(lengths)}")
    report(cv >= 0.35,
           f"sentence-length variation (CV {cv:.2f}) — "
           + ("healthy spread" if cv >= 0.35 else
              "uniform lengths; the most consistent statistical AI tell"))
    if len(lengths) >= 8:
        short_cut, long_cut = (8, 40) if lang == "zh" else (6, 25)
        report(min(lengths) < short_cut,
               f"has a short sentence (<{short_cut} {unit})" if
               min(lengths) < short_cut else
               f"no sentence under {short_cut} {unit} — mix in a short one")
        report(max(lengths) > long_cut,
               f"has a long sentence (>{long_cut} {unit})" if
               max(lengths) > long_cut else
               f"no sentence over {long_cut} {unit} — let one breathe")


def check_openers(sentences, lang):
    if lang == "zh" or len(sentences) < 5:
        return
    section("Sentence openers")
    firsts = []
    for s in sentences:
        m = re.match(r"[^A-Za-zÀ-ÖØ-öø-ÿ]*([A-Za-zÀ-ÖØ-öø-ÿ']+)", s)
        if m:
            firsts.append(m.group(1).lower())
    if not firsts:
        return
    top, count = max(((w, firsts.count(w)) for w in set(firsts)),
                     key=lambda x: x[1])
    share = count / len(firsts)
    report(share <= 0.3 or count < 3,
           f'most common opener "{top}" starts {count}/{len(firsts)} '
           f"sentences" + ("" if share <= 0.3 or count < 3
                           else " — vary the openings"))


def check_paragraphs(paragraphs, lang):
    if len(paragraphs) < 4:
        return
    section("Paragraphs")
    sizes = [len(split_sentences(p, lang)) for p in paragraphs]
    mean = statistics.mean(sizes)
    cv = round(statistics.pstdev(sizes) / mean, 2) if mean else 0
    report(cv >= 0.25,
           f"paragraph sizes {sizes} (CV {cv:.2f}) — "
           + ("varied" if cv >= 0.25
              else "uniform; human paragraphs range from 1 line to 10"))


def check_vocabulary(text, lang):
    section("AI vocabulary")
    words, phrases, watch = {
        "en": (AI_WORDS_EN, AI_PHRASES_EN, AI_WATCH_EN),
        "de": (AI_WORDS_DE, AI_PHRASES_DE, AI_WATCH_DE),
        "zh": ([], AI_PHRASES_ZH, AI_WATCH_ZH),
    }[lang]
    hits = count_hits(text, words, phrases, lang)
    if hits:
        shown = ", ".join(f"{w} ×{n}" for w, n in hits[:8])
        extra = f" (+{len(hits) - 8} more)" if len(hits) > 8 else ""
        report(len(hits) <= 1 and hits[0][1] <= 1, f"catalog hits: {shown}{extra}")
    else:
        report(True, "no catalog vocabulary found")
    seen = count_hits(text, watch, [], lang)
    if seen:
        note("watchlist (context-dependent, not flagged): "
             + ", ".join(f"{w} ×{n}" for w, n in seen[:8]))


def check_punctuation(original, folded, lang, sentences):
    section("Punctuation")
    if lang == "de":
        em = original.count("—")
        report(em == 0,
               "no em-dash (Geviertstrich)" if em == 0 else
               f"{em} Geviertstrich(e) — German uses – with spaces")
        loose = len(re.findall(r"(?<=\S) (?:-|--) (?=\S)", original))
        report(loose == 0,
               "no hyphen used as a dash" if loose == 0 else
               f"{loose} hyphen(s) used as a dash — German uses – with spaces")
        german = original.count("„")
        guillemets = original.count("»") + original.count("«")
        english = original.count("”") + len(
            re.findall(r"(?:^|[\s(\[–—-])“", original, re.M))
        straight = original.count('"')
        if english or straight:
            parts = []
            if english:
                parts.append(f"{english} English curly quote(s)")
            if straight:
                parts.append(f"{straight} straight quote(s)")
            report(False, " and ".join(parts) + " — German prose uses „…“")
        elif german and guillemets:
            report(False, "mixed „…“ and »…« — pick one")
        else:
            report(True, "quotation marks consistent")
    elif lang == "zh":
        half = len(re.findall(rf"[{CJK}][,\.;:!\?]", original))
        report(half == 0,
               "no half-width punctuation after Chinese characters"
               if half == 0 else
               f"{half} half-width mark(s) inside Chinese text — "
               "use full-width")
        semis = original.count("；")
        report(semis <= max(1, len(sentences) // 10),
               f"{semis} Chinese semicolon(s)" + (
                   "" if semis <= max(1, len(sentences) // 10)
                   else " — AI overuses ；"))
        if "“" in original and "「" in original:
            report(False, "mixed “” and 「」 quote styles — pick one")
    else:
        em = original.count("—")
        per_sent = em / max(1, len(sentences))
        report(per_sent <= 0.2,
               f"{em} em-dash(es) across {len(sentences)} sentences" + (
                   "" if per_sent <= 0.2 else " — thin them out"))
        curly_q = original.count("“") + original.count("”")
        straight_q = original.count('"')
        if curly_q and straight_q:
            report(False, "mixed curly and straight quotes — pick one")
        curly_ap = original.count("’")
        straight_ap = len(re.findall(r"(?<=\w)'(?=\w)", original))
        if curly_ap and straight_ap:
            report(False, "mixed curly and straight apostrophes — pick one")


def check_language_flavor(original, folded, lang, sentences):
    if lang == "zh":
        section("Chinese flavor (informational)")
        particles = sum(1 for s in sentences if s and s[-1] in ZH_PARTICLES)
        note(f"sentence-final particles (呢/啊/吧/嘛…): {particles} — "
             "not a quota. A particle bolted onto a sentence that was never "
             "spoken (\"辛苦了啊\") reads more artificial than none at all, "
             "and email, announcements and reports are not informal text. "
             "Zero is the right answer more often than not")
    elif lang == "de":
        section("German flavor (informational)")
        n = len(re.findall(
            r"\b(" + "|".join(DE_MODAL_PARTICLES) + r")\b", folded))
        note(f"modal particle hits (doch/halt/mal/eben…): {n} — "
             "zero in informal text is a strong AI tell; "
             "in formal text zero is correct")
    else:
        section("English flavor (informational)")
        short = len(re.findall(
            r"\b(don't|it's|can't|won't|isn't|we're|i'm|didn't|doesn't"
            r"|you're|that's|there's|wasn't|aren't|couldn't|wouldn't"
            r"|they're|we've|i've|let's|he's|she's|hasn't|haven't)\b", folded))
        full = len(re.findall(
            r"\b(do not|it is|cannot|can not|will not|is not|we are|i am"
            r"|did not|does not|you are|that is|there is|was not|are not"
            r"|could not|would not|they are|we have|i have|let us|has not"
            r"|have not)\b", folded))
        note(f"contractions {short} vs full forms {full} — "
             "all-full-forms in casual prose reads machine or lawyer")


# ---------------------------------------------------------------- fidelity --
# Words that begin a sentence or are grammatically capitalized, so seeing them
# capitalized proves nothing about them being a name.
CAP_STOPWORDS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "he", "her",
    "his", "i", "if", "in", "is", "it", "its", "my", "no", "not", "of", "on",
    "or", "our", "she", "so", "that", "the", "their", "then", "there", "they",
    "this", "to", "we", "what", "when", "where", "which", "who", "why",
    "with", "yes", "you", "your", "every", "most", "some", "one", "two",
    "der", "die", "das", "und", "wir", "sie", "ich", "es", "ein", "eine",
    "der", "den", "dem", "aber", "auch", "nicht", "wenn", "dann", "hier",
}
ATTRIBUTION_RE = {
    "en": r"\b(according to|observers?|experts?|critics?|analysts?|"
          r"researchers?|stud(?:y|ies)|survey|industry reports?|"
          r"sources?|cited|reported|said|says|argues?|claims?|"
          r"noted|per the)\b",
    "de": r"\b(laut|zufolge|Beobachter|Branchenexperten|Expert(?:en|innen)|"
          r"Kritiker|Studien? (?:zeigen|zeigt)|Forschung zeigt|berichtet|"
          r"sagte|sagt)\b",
    "zh": r"(据|根据|表示|认为|指出|业内人士|专家|观察人士|研究表明|"
          r"报道称|调查显示|数据显示)",
}
COMMITMENT_RE = {
    "en": r"\b(we(?:'ll| will| are going to| shall)|i(?:'ll| will)|"
          r"you(?:'ll| will) (?:receive|get|see))\b",
    "de": r"\b(wir werden|ich werde|wir kümmern uns|wir melden uns)\b",
    "zh": r"(我们会|我们将|我会|我将|接下来会|后续会)",
}
# Absolutes and totalising words. Present in the rewrite but not the source
# means the rewrite raised the stakes on its own.
SEVERITY = {
    "en": ["nothing", "never", "always", "everyone", "nobody", "completely",
           "entirely", "totally", "catastrophic", "disaster", "all of",
           "every single", "zero", "no one", "worst", "impossible"],
    "de": ["nichts", "nie", "niemals", "immer", "jeder", "niemand", "völlig",
           "komplett", "katastrophal", "unmöglich", "schlimmste"],
    "zh": ["完全", "彻底", "从来没有", "永远", "所有人", "没有人", "灾难",
           "最差", "不可能", "全部"],
}


CONTRACTION_RE = re.compile(r"['’](ve|d|ll|s|m|re|t)$", re.I)


def fidelity_tokens(text, lang, generous=False):
    """Names, numbers and dates, as comparable normalized tokens.

    generous=True also accepts sentence-initial capitals. Use it on the
    source so a name that happens to open a sentence there ("Stack Overflow
    provided...") still counts as known; use it off on the rewrite so an
    ordinary word opening a sentence is not mistaken for an invented name.

    Known limitation: an invented name that opens a sentence in the rewrite
    ("Acme rebuilt the flow.") is not flagged, because nothing distinguishes
    it from an ordinary capitalized opener without a dictionary. False
    positives are worse than misses in a gate, so this errs toward silence;
    catalog pattern 43 covers the case in prose.
    """
    numbers = set()
    for raw in re.findall(r"\d[\d,]*(?:[.:]\d+)?%?", text):
        n = raw.rstrip(".,").replace(",", "")
        if n:
            numbers.add(n)
            numbers.add(n.rstrip("%"))
    names = set()
    if lang != "zh":
        for sentence in re.split(r"(?<=[.!?])\s+|\n", text):
            words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ][\w'’\-]*", sentence)
            for i, w in enumerate(words):
                if not w[0].isupper() or (i == 0 and not generous):
                    continue
                stem = CONTRACTION_RE.sub("", w).lower()
                if not stem or stem in CAP_STOPWORDS:
                    continue
                names.add(stem)
    return names, numbers


def source_acronyms(source):
    """"artificial intelligence" in the source licenses "AI" in the rewrite."""
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", source)
    out = set()
    for size in (2, 3, 4):
        for i in range(len(words) - size + 1):
            run = words[i:i + size]
            if all(w.lower() not in CAP_STOPWORDS for w in run):
                out.add("".join(w[0] for w in run).lower())
    return out


def orphaned_claims(source, output, lang):
    """Attributed claims in the source that survive in the rewrite unattributed.

    Dropping an attribution is only theft if the claim comes with it. A
    rewrite that cuts "observers have cited X as a barrier" outright is doing
    exactly what the catalog asks, and must not be flagged for it.
    """
    attr = re.compile(ATTRIBUTION_RE[lang], re.I)
    out_low = output.lower()
    orphans = []
    for sentence in split_sentences(source, lang):
        if not attr.search(sentence):
            continue
        body = attr.sub(" ", sentence)
        if lang == "zh":
            terms = [t for t in re.findall(rf"[{CJK}]{{2,}}", body)
                     if len(t) >= 2]
        else:
            terms = [w.lower() for w in WORD_RE.findall(body)
                     if len(w) > 3 and w.lower() not in CAP_STOPWORDS]
        if not terms:
            continue
        kept = sum(1 for t in terms if t in out_low)
        # Half the claim's distinctive words still present, and nobody is
        # credited anywhere in the rewrite: the rewrite adopted the claim.
        if kept / len(terms) >= 0.5 and not attr.search(output):
            orphans.append(sentence.strip()[:70])
    return orphans


def check_fidelity(source, output, lang):
    section("Fidelity (rewrite vs original)")
    src_names, src_nums = fidelity_tokens(source, lang, generous=True)
    out_names, out_nums = fidelity_tokens(output, lang)

    acronyms = source_acronyms(source)
    new_names = sorted(n for n in out_names - src_names
                       if n not in acronyms
                       and not any(n in s or s in n for s in src_names))
    report(not new_names,
           "no names in the rewrite that are absent from the original"
           if not new_names else
           "names not in the original: " + ", ".join(new_names[:8])
           + " — invented, or confirm each is a form of a source name")

    new_nums = sorted(n for n in out_nums - src_nums)
    report(not new_nums,
           "no figures in the rewrite that are absent from the original"
           if not new_nums else
           "figures not in the original: " + ", ".join(new_nums[:8])
           + " — invented, or confirm each is derived from source figures")

    stolen = orphaned_claims(source, output, lang)
    report(not stolen,
           "no attributed claim was taken over as the rewrite's own"
           if not stolen else
           f"{len(stolen)} attributed claim(s) kept without the attribution: "
           + "; ".join(f'"{s}"' for s in stolen[:2])
           + " — cut the claim with the attribution, or keep the attribution")

    src_com = set(m.lower() for m in
                  re.findall(COMMITMENT_RE[lang], source, re.I))
    out_com = set(m.lower() for m in
                  re.findall(COMMITMENT_RE[lang], output, re.I))
    new_com = sorted(out_com - src_com)
    report(not new_com,
           "no promises the original did not make" if not new_com else
           "new commitment(s): " + ", ".join(new_com[:5])
           + " — the original promised nothing here")

    low = output.lower()
    src_low = source.lower()
    esc = [w for w in SEVERITY[lang] if w in low and w not in src_low]
    report(not esc,
           "severity matches the original" if not esc else
           "raised severity: " + ", ".join(esc[:6])
           + " — the original did not go this far")


# Catalog entries that describe a syntactic shape rather than a string, so no
# word list can ever cover them. The model reads these; the checker cannot.
AUDIT_STRUCTURAL = [
    "名词化表达", "被动句滥用", "每句都从主语起头", "过长的",
    "把该连成一口气的流水句",
]

CATALOG_MARKERS = [
    r"Words to watch:", r"Wörter:", r"Hochfrequente KI-Wörter:",
    r"Hochfrequente KI-Konnektoren:", r"Todesphrasen(?: \([^)]*\))?:",
    r"Auch Pseudo-Einsicht-Auftakte:", r"Signal:",
    r"需要注意的套语：", r"需要注意：", r"高频 AI 连接词：", r"如：",
    r"也要注意假洞察开场：",
]


def catalog_terms(path):
    text = Path(path).read_text(encoding="utf-8")
    marker = re.compile("(?:" + "|".join(CATALOG_MARKERS) + r")(.*)")
    terms = []
    for line in text.split("\n"):
        m = marker.search(line)
        if not m:
            continue
        body = re.sub(r"[（(][^）)]*[）)]", "", m.group(1))
        for raw in re.split(r"[,、，]", body):
            term = raw.strip().strip('"“”「」').strip(".。…").strip()
            # Some catalog entries describe a shape rather than a string
            # ("过长的'的'字串"); an ellipsis is the reliable marker.
            if "…" in term or "..." in term or term.startswith("http"):
                continue
            min_len = 2 if CJK_RE.search(term) else 3
            if len(term) < min_len:
                continue
            # "stands/serves as" documents two phrasings, not one term.
            terms.extend(p for p in expand_alternatives(term)
                         if len(p) >= min_len)
    return sorted(set(terms))


def expand_alternatives(term):
    """"stands/serves as" -> ["stands as", "serves as"]."""
    tokens = term.split(" ")
    for i, token in enumerate(tokens):
        if "/" in token:
            return [" ".join(tokens[:i] + [alt] + tokens[i + 1:])
                    for alt in token.split("/") if alt]
    return [term]


def run_audit(lang, catalog):
    words, phrases, watch = {
        "en": (AI_WORDS_EN, AI_PHRASES_EN, AI_WATCH_EN),
        "de": (AI_WORDS_DE, AI_PHRASES_DE, AI_WATCH_DE),
        "zh": ([], AI_PHRASES_ZH, AI_WATCH_ZH),
    }[lang]
    # SEVERITY is checked by the fidelity pass rather than the vocabulary
    # pass, but it is still covered — the audit should not report it missing.
    known = fold(" ".join(words + phrases + watch + SEVERITY[lang]))
    terms = [t for t in catalog_terms(catalog)
             if not any(t.startswith(s) for s in AUDIT_STRUCTURAL)]
    missing = []
    for term in terms:
        probe = fold(term)
        if lang == "zh":
            covered = any(p in probe or probe in p
                          for p in [fold(x)
                                    for x in phrases + watch + SEVERITY[lang]])
        else:
            head = probe.split()[0] if probe.split() else probe
            covered = probe in known or re.search(
                rf"\b{re.escape(head[:max(4, len(head) - 3)])}", known)
        if not covered:
            missing.append(term)
    print(f"catalog audit · {catalog}")
    print(f"  · {len(terms)} matchable term(s) documented in the catalog")
    if missing:
        print(f"  ⚠ {len(missing)} not visible to the checker:")
        for term in missing:
            print(f"      {term}")
        print("\n  Add the important ones to AI_WORDS_* / AI_PHRASES_* "
              "(flagged)\n  or AI_WATCH_* (reported only).")
    else:
        print("  · every catalog term is covered")
    return 1 if missing else 0


def main():
    parser = argparse.ArgumentParser(
        description="Statistical AI-tell screening for EN/ZH/DE text.")
    parser.add_argument("file", nargs="?", help="text file to screen")
    parser.add_argument("--source",
                        help="the original text, to run the fidelity pass")
    parser.add_argument("--lang", choices=["en", "zh", "de"],
                        help="language (default: auto-detect)")
    parser.add_argument("--json", action="store_true",
                        help="emit the report as JSON")
    parser.add_argument("--audit", action="store_true",
                        help="compare word lists against references/patterns.md")
    parser.add_argument("--catalog",
                        help="catalog path for --audit "
                             "(default: ../references/patterns.md)")
    args = parser.parse_args()

    if args.audit:
        catalog = args.catalog or (
            Path(__file__).resolve().parent.parent / "references"
            / "patterns.md")
        if not Path(catalog).exists():
            sys.exit(f"error: catalog not found: {catalog}")
        lang = args.lang or detect_lang(
            Path(catalog).read_text(encoding="utf-8"))
        sys.exit(run_audit(lang, catalog))

    if not args.file:
        parser.error("a FILE is required unless --audit is used")
    try:
        raw = Path(args.file).read_text(encoding="utf-8")
    except OSError as e:
        sys.exit(f"error: {e}")
    if not raw.strip():
        sys.exit("error: file is empty")

    text, stripped = strip_markdown(raw)
    if not text.strip():
        sys.exit("error: nothing left after removing markdown scaffolding")
    folded = fold(text)
    lang = args.lang or detect_lang(text)
    paragraphs = split_paragraphs(text)
    sentences = [s for p in paragraphs for s in split_sentences(p, lang)]

    dropped = ", ".join(f"{n} {name}" for name, n in stripped.items() if n)
    print(f"naturalness-check · language: {lang} · "
          f"{len(paragraphs)} paragraph(s), {len(sentences)} sentence(s)"
          + (f" · skipped {dropped}" if dropped else ""))

    check_rhythm(sentences, lang)
    check_openers(sentences, lang)
    check_paragraphs(paragraphs, lang)
    check_vocabulary(folded, lang)
    check_punctuation(text, folded, lang, sentences)
    check_language_flavor(text, folded, lang, sentences)
    if args.source:
        try:
            src = strip_markdown(
                Path(args.source).read_text(encoding="utf-8"))[0]
        except OSError as e:
            sys.exit(f"error: --source: {e}")
        check_fidelity(src, text, lang)

    print(f"\n{len(flags)} warning(s)." if flags else
          "\nNo warnings. (Signals only — read it aloud anyway.)")

    if args.json:
        print(json.dumps({
            "file": args.file,
            "lang": lang,
            "paragraphs": len(paragraphs),
            "sentences": len(sentences),
            "skipped": stripped,
            "sections": sections,
            "warnings": flags,
            "ok": not flags,
        }, ensure_ascii=False, indent=2))

    sys.exit(1 if flags else 0)


if __name__ == "__main__":
    main()
