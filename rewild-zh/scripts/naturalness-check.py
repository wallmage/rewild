#!/usr/bin/env python3
"""Naturalness check: statistical AI-tell screening for EN / ZH / DE text.

Usage:
    python3 naturalness-check.py FILE [--lang en|zh|de]

Screens a text for the measurable signals described in the Rewild pattern
catalogs: sentence-length uniformity, repeated sentence openers, uniform
paragraph sizes, AI vocabulary, and punctuation problems. Zero dependencies.

It measures signals, not truth. A clean report does not prove the text reads
well, and a single warning does not condemn it. Judgment stays with the writer.
"""

import argparse
import re
import statistics
import sys
import unicodedata

AI_WORDS_EN = [
    "additionally", "moreover", "furthermore", "delve", "testament",
    "pivotal", "crucial", "seamless", "leverage", "robust", "holistic",
    "myriad", "realm", "tapestry", "underscore", "underscores", "showcase",
    "showcases", "fostering", "garner", "groundbreaking", "vibrant",
    "cutting-edge", "game-changing", "elevate", "streamline", "boasts",
]
AI_PHRASES_EN = [
    "it's worth noting", "it is worth noting", "it's important to note",
    "it is important to note", "in today's", "in conclusion", "in summary",
    "not only", "plays a crucial role", "stands as a", "serves as a",
    "ever-evolving", "fast-paced world",
]
AI_WORDS_DE = [
    "zudem", "folglich", "nichtsdestotrotz", "zusammenfassend",
    "abschließend", "infolgedessen", "innovativ", "nahtlos", "ganzheitlich",
    "bahnbrechend", "facettenreich", "maßgeblich", "essenziell",
    "meilenstein",
]
AI_PHRASES_DE = [
    "darüber hinaus", "in der heutigen zeit", "im digitalen zeitalter",
    "es ist wichtig zu beachten", "tauchen wir ein", "eine vielzahl",
    "breite palette", "nicht nur", "schlüsselrolle", "lässt sich sagen",
]
AI_PHRASES_ZH = [
    "此外", "值得注意的是", "值得一提的是", "综上所述", "总而言之",
    "总的来说", "与此同时", "不难发现", "在当今", "众所周知", "赋能",
    "砥砺前行", "不忘初心", "深耕细作", "精益求精", "高质量发展",
    "开拓创新", "与时俱进", "未来可期", "我们有理由相信", "深刻变革",
    "不可忽视", "近年来，随着", "随着人工智能",
]
ZH_PARTICLES = "呢啊吧嘛哦啦哇喽呀"
DE_MODAL_PARTICLES = [
    "doch", "halt", "mal", "eben", "ja", "schon", "wohl", "eigentlich",
    "übrigens",
]

flags = []


def report(ok, message):
    marker = "  ·" if ok else "  ⚠"
    if not ok:
        flags.append(message)
    print(f"{marker} {message}")


def is_cjk(ch):
    return "CJK" in unicodedata.name(ch, "")


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


def split_sentences(text, lang):
    if lang == "zh":
        parts = re.split(r"[。！？…]+", text)
    else:
        parts = re.split(r"(?<=[.!?])[\"'”’)\]]*\s+", text)
    return [s.strip() for s in parts if s.strip()]


def sentence_length(sentence, lang):
    if lang == "zh":
        return sum(1 for c in sentence if is_cjk(c))
    return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-ž']+", sentence))


def check_rhythm(sentences, lang):
    print("\nRhythm")
    lengths = [sentence_length(s, lang) for s in sentences]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 4:
        print("  · too few sentences for rhythm statistics")
        return
    mean = statistics.mean(lengths)
    stdev = statistics.pstdev(lengths)
    cv = stdev / mean if mean else 0
    unit = "chars" if lang == "zh" else "words"
    print(f"  · {len(lengths)} sentences, mean {mean:.1f} {unit}, "
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
    print("\nSentence openers")
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
    print("\nParagraphs")
    sizes = [len(split_sentences(p, lang)) for p in paragraphs]
    mean = statistics.mean(sizes)
    cv = statistics.pstdev(sizes) / mean if mean else 0
    report(cv >= 0.25 or len(set(sizes)) > 2,
           f"paragraph sizes {sizes} — "
           + ("varied" if cv >= 0.25 or len(set(sizes)) > 2
              else "uniform; human paragraphs range from 1 line to 10"))


def count_hits(text, words, phrases, boundary):
    lower = text.lower()
    hits = []
    for w in words:
        n = len(re.findall(rf"\b{re.escape(w)}\b", lower)) if boundary \
            else lower.count(w)
        if n:
            hits.append((w, n))
    for p in phrases:
        n = lower.count(p)
        if n:
            hits.append((p, n))
    return sorted(hits, key=lambda x: -x[1])


def check_vocabulary(text, lang):
    print("\nAI vocabulary")
    if lang == "en":
        hits = count_hits(text, AI_WORDS_EN, AI_PHRASES_EN, True)
    elif lang == "de":
        hits = count_hits(text, AI_WORDS_DE, AI_PHRASES_DE, True)
    else:
        hits = count_hits(text, [], AI_PHRASES_ZH, False)
    if not hits:
        report(True, "no catalog vocabulary found")
        return
    shown = ", ".join(f"{w} ×{n}" for w, n in hits[:8])
    report(len(hits) <= 1 and hits[0][1] <= 1,
           f"catalog hits: {shown}")


def check_punctuation(text, lang, sentences):
    print("\nPunctuation")
    em = text.count("—")
    if lang == "de":
        report(em == 0,
               "no em-dash (Geviertstrich)" if em == 0 else
               f"{em} Geviertstrich(e) — German uses – with spaces")
        straight = len(re.findall(r'"', text))
        proper = text.count("„")
        if straight and not proper:
            report(False, f'{straight} straight quote(s) — German prose '
                          "uses „…“")
        elif straight and proper:
            report(False, "mixed „…“ and straight quotes — pick one")
        else:
            report(True, "quotation marks consistent")
    elif lang == "zh":
        cjk_half = len(re.findall(r"[一-鿿][,\.;:!\?]", text))
        report(cjk_half == 0,
               "no half-width punctuation after Chinese characters"
               if cjk_half == 0 else
               f"{cjk_half} half-width mark(s) inside Chinese text — "
               "use full-width")
        semis = text.count("；")
        report(semis <= max(1, len(sentences) // 10),
               f"{semis} Chinese semicolon(s)" + (
                   "" if semis <= max(1, len(sentences) // 10)
                   else " — AI overuses ；"))
        if "“" in text and "「" in text:
            report(False, "mixed “” and 「」 quote styles — pick one")
    else:
        per_sent = em / max(1, len(sentences))
        report(per_sent <= 0.2,
               f"{em} em-dash(es) across {len(sentences)} sentences" + (
                   "" if per_sent <= 0.2 else " — thin them out"))
        if "“" in text and re.search(r'\w"', text):
            report(False, "mixed curly and straight quotes — pick one")


def check_language_flavor(text, lang, sentences):
    if lang == "zh":
        print("\nChinese flavor (informational)")
        particles = sum(1 for s in sentences if s and s[-1] in ZH_PARTICLES)
        print(f"  · sentence-final particles (呢/啊/吧/嘛…): {particles} — "
              "zero in informal text is a strong AI tell; "
              "in formal text zero is correct")
    elif lang == "de":
        print("\nGerman flavor (informational)")
        n = len(re.findall(
            r"\b(" + "|".join(DE_MODAL_PARTICLES) + r")\b", text.lower()))
        print(f"  · modal particle hits (doch/halt/mal/eben…): {n} — "
              "zero in informal text is a strong AI tell; "
              "in formal text zero is correct")
    else:
        informal = len(re.findall(
            r"\b(don't|it's|can't|won't|isn't|we're|i'm|didn't|doesn't"
            r"|you're|that's|there's|wasn't|aren't|couldn't|wouldn't)\b",
            text.lower()))
        full = len(re.findall(
            r"\b(do not|it is|cannot|will not|is not|we are|i am|did not"
            r"|does not|you are|that is|there is)\b", text.lower()))
        print("\nEnglish flavor (informational)")
        print(f"  · contractions {informal} vs full forms {full} — "
              "all-full-forms in casual prose reads machine or lawyer")


def main():
    parser = argparse.ArgumentParser(
        description="Statistical AI-tell screening for EN/ZH/DE text.")
    parser.add_argument("file", help="text file to screen")
    parser.add_argument("--lang", choices=["en", "zh", "de"],
                        help="language (default: auto-detect)")
    args = parser.parse_args()

    try:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        sys.exit(f"error: {e}")
    if not text.strip():
        sys.exit("error: file is empty")

    lang = args.lang or detect_lang(text)
    paragraphs = split_paragraphs(text)
    sentences = [s for p in paragraphs for s in split_sentences(p, lang)]

    print(f"naturalness-check · language: {lang} · "
          f"{len(paragraphs)} paragraph(s), {len(sentences)} sentence(s)")

    check_rhythm(sentences, lang)
    check_openers(sentences, lang)
    check_paragraphs(paragraphs, lang)
    check_vocabulary(text, lang)
    check_punctuation(text, lang, sentences)
    check_language_flavor(text, lang, sentences)

    print(f"\n{len(flags)} warning(s)." if flags else
          "\nNo warnings. (Signals only — read it aloud anyway.)")


if __name__ == "__main__":
    main()
