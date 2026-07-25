#!/usr/bin/env python3
"""Regression tests for scripts/naturalness-check.py.

Every case here is a bug the checker actually shipped with. Run from the repo
root with no arguments:

    python3 tests/test_checker.py

Zero dependencies, no test framework.
"""

import importlib.util
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ["rewild", "rewild-zh", "rewild-de"]


def load(path):
    spec = importlib.util.spec_from_file_location("checker", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


chk = load(ROOT / SKILLS[0] / "scripts" / "naturalness-check.py")
results = []


def check(name, condition, detail=""):
    results.append((name, condition, detail))
    print(f"{'  ok  ' if condition else '  FAIL'}  {name}"
          + (f"  — {detail}" if detail and not condition else ""))


def scan(text, lang):
    """Run the full pipeline and return (warning messages, all messages)."""
    chk.sections.clear()
    chk.flags.clear()
    stripped, _ = chk.strip_markdown(text)
    folded = chk.fold(stripped)
    paragraphs = chk.split_paragraphs(stripped)
    sentences = [s for p in paragraphs for s in chk.split_sentences(p, lang)]
    with redirect_stdout(io.StringIO()):
        chk.check_rhythm(sentences, lang)
        chk.check_openers(sentences, lang)
        chk.check_paragraphs(paragraphs, lang)
        chk.check_vocabulary(folded, lang)
        chk.check_punctuation(stripped, folded, lang, sentences)
        chk.check_language_flavor(stripped, folded, lang, sentences)
    warnings = " | ".join(f["message"] for f in chk.flags)
    everything = " | ".join(
        line["message"] for s in chk.sections for line in s["lines"])
    return warnings, everything


# 1 — smart apostrophes must not hide catalog phrases or contractions.
SMART = ("In today’s fast-paced world, it’s worth noting that we "
         "don’t ship slop. It’s important to note that we can’t "
         "always tell. That’s the job. We won’t pretend otherwise.")
warn, allmsg = scan(SMART, "en")
check("smart apostrophes: catalog phrases still match",
      "in today's" in warn and "it's worth noting" in warn, warn)
check("smart apostrophes: contractions counted",
      "contractions 6" in allmsg, allmsg)

# 2 — AI vocabulary survives inflection.
INFLECTED = ("The team is leveraging a streamlined workflow. Underscoring the "
             "value, the platform showcases robust tooling and fosters "
             "collaboration. Delving into the details reveals a comprehensive "
             "approach. This elevates the experience. Boasting a myriad of "
             "features, it handles the intricate work.")
found = dict(chk.count_hits(chk.fold(INFLECTED), chk.AI_WORDS_EN,
                            chk.AI_PHRASES_EN, "en"))
wanted = ["leveraging", "streamlined", "underscoring", "showcases",
          "fosters", "delving", "comprehensive", "elevates", "boasting",
          "myriad", "intricate", "robust"]
missed = [w for w in wanted if w not in found]
check("inflected AI vocabulary detected", not missed, f"missed {missed}")

# 3 — abbreviations do not end sentences.
ABBR = "Dr. Chen shipped it on Jan. 3 at 4 p.m. The U.S. team followed."
check("abbreviations do not split sentences",
      len(chk.split_sentences(ABBR, "en")) == 2,
      str(chk.split_sentences(ABBR, "en")))
check("decimals do not split sentences",
      len(chk.split_sentences("Version 2.5 landed. It works.", "en")) == 2)

# 4 — markdown scaffolding is not prose.
MD = ("# Heading\n\nReal prose here.\n\n- one\n- two\n\n"
      "| a | b |\n\n```\ncode();\n```\n\nMore prose.")
text, stats = chk.strip_markdown(MD)
check("markdown: heading dropped", stats["heading"] == 1, str(stats))
check("markdown: code fence dropped",
      stats["code"] == 1 and "code()" not in text, str(stats))
check("markdown: table row dropped", stats["table"] == 1, str(stats))
check("markdown: list items terminated",
      len(chk.split_sentences("one.\ntwo.", "en")) == 2 and "one." in text,
      repr(text))

# 5 — Chinese sentence length counts non-Han tokens too. Han-only counting
# undercounted mixed-script technical Chinese by a third or more.
ZH = "我们用 Kubernetes 做容器编排，配合 Prometheus 和 Grafana 做监控"
han_only = len(chk.CJK_RE.findall(ZH))
check("zh length counts latin tokens",
      chk.sentence_length(ZH, "zh") == han_only + 3,
      f"got {chk.sentence_length(ZH, 'zh')}, han-only is {han_only}")

# 6 — German quotation and dash conventions.
warn, _ = scan('Er sagte: “Das stimmt.” Die Sache ist gut. '
               'Das Team hat geliefert. Alles lief rund.', "de")
check("de: English curly quotes flagged", "English curly quote" in warn, warn)
warn, _ = scan("Die Ergebnisse - sauber und effizient - sprechen für sich. "
               "Wir haben geliefert. Der Kunde war zufrieden.", "de")
check("de: hyphen used as dash flagged", "used as a dash" in warn, warn)
warn, _ = scan('Er sagte: „Das stimmt.“ Die Sache ist gut. '
               'Das Team hat geliefert. Alles lief rund.', "de")
check("de: correct „…“ passes", "quote" not in warn, warn)

# 7 — paragraph uniformity has no escape hatch.
UNIFORM = "\n\n".join(["A one two. B one two. C one two.",
                       "D one two. E one two. F one two. G one.",
                       "H one two. I one two.",
                       "J one two. K one two. L one two.",
                       "M one two. N one two. O one two."])
warn, _ = scan(UNIFORM, "en")
check("uniform paragraph sizes flagged", "paragraph sizes" in warn, warn)

# 8 — good human prose is left alone.
CLEAN = ("The migration took three weekends instead of one. Most of the delay "
         "came from the auth service, which nobody had touched since 2019. We "
         "found the problem in a config file that overrode staging.\n\n"
         "I don't think we'd do it the same way again. Splitting the cutover "
         "across two Saturdays would have cost less sleep.\n\n"
         "Anyway, it's done. The service has been up for six weeks.")
warn, _ = scan(CLEAN, "en")
check("clean human prose raises no warnings", not warn, warn)

# 9 — the three shipped copies stay byte-identical.
digests = {p: (ROOT / p / "scripts" / "naturalness-check.py").read_bytes()
           for p in SKILLS}
check("all three skill copies identical",
      len(set(digests.values())) == 1,
      ", ".join(p for p in digests))

# 10 — every catalog term the checker can match is covered.
for skill, lang in zip(SKILLS, ["en", "zh", "de"]):
    catalog = ROOT / skill / "references" / "patterns.md"
    with redirect_stdout(io.StringIO()):
        missing = chk.run_audit(lang, catalog)
    check(f"catalog audit clean ({lang})", missing == 0,
          "run --audit to see the terms")

failed = [name for name, ok, _ in results if not ok]
print(f"\n{len(results) - len(failed)}/{len(results)} passed.")
sys.exit(1 if failed else 0)
