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
SKILLS = ["rewild", "rewild-zh", "rewild-de", "rewild-hk", "rewild-tw"]
SKILL_LANGS = ["en", "zh", "de", "hk", "tw"]


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
        chk.check_region(stripped, lang)
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

# 9 — every shipped copy stays byte-identical.
digests = {p: (ROOT / p / "scripts" / "naturalness-check.py").read_bytes()
           for p in SKILLS}
check(f"all {len(SKILLS)} skill copies identical",
      len(set(digests.values())) == 1,
      ", ".join(p for p in digests))

# 10 — every catalog term the checker can match is covered.
for skill, lang in zip(SKILLS, SKILL_LANGS):
    catalog = ROOT / skill / "references" / "patterns.md"
    if not catalog.exists():
        check(f"catalog audit clean ({lang})", False, f"missing {catalog}")
        continue
    with redirect_stdout(io.StringIO()):
        missing = chk.run_audit(lang, catalog)
    check(f"catalog audit clean ({lang})", missing == 0,
          "run --audit to see the terms")

# 11 — the fidelity pass. Each case is a failure observed in a real rewrite.
def fid(source, output, lang="en"):
    chk.sections.clear()
    chk.flags.clear()
    with redirect_stdout(io.StringIO()):
        chk.check_fidelity(source, output, lang)
    return " | ".join(f["message"] for f in chk.flags)

SRC = ("Observers have cited onboarding friction as a barrier. Setup took 45 "
       "minutes. The change was deployed by the platform team and impacted "
       "the primary cluster.")

_inv = "Observers cited it. The flow was rebuilt by Acme last month."
check("fidelity: invented name flagged", "acme" in fid(SRC, _inv), fid(SRC, _inv))
# Documented limitation: a sentence-initial invented name is not flagged,
# because nothing separates it from an ordinary capitalized opener.
_ini = "Observers cited it. Acme rebuilt the flow."
check("fidelity: sentence-initial invented name is a known miss",
      "acme" not in fid(SRC, _ini), fid(SRC, _ini))
check("fidelity: invented figure flagged",
      "figures not in the original" in fid(SRC, "Setup took 12 minutes."),
      fid(SRC, "Setup took 12 minutes."))
_theft = "Onboarding friction is the barrier. Setup took 45 minutes."
check("fidelity: attribution theft flagged",
      "without the attribution" in fid(SRC, _theft), fid(SRC, _theft))
# Cutting the claim along with its attribution is correct, not theft.
_cut = "Setup took 45 minutes, and now it is faster."
check("fidelity: claim cut with its attribution passes",
      "without the attribution" not in fid(SRC, _cut), fid(SRC, _cut))
check("fidelity: invented commitment flagged",
      "commitment" in fid(SRC, "Setup took 45 minutes. We'll fix it."),
      fid(SRC, "Setup took 45 minutes. We'll fix it."))
check("fidelity: severity inflation flagged",
      "severity" in fid(SRC, "Nothing worked for the whole cluster."),
      fid(SRC, "Nothing worked for the whole cluster."))
_ok = ("Setup took 45 minutes. The platform team's deploy hit the primary "
       "cluster, and observers called that friction a barrier.")
check("fidelity: faithful rewrite passes", not fid(SRC, _ok), fid(SRC, _ok))
check("fidelity: identical text passes", not fid(SRC, SRC), fid(SRC, SRC))
check("fidelity: acronym of a source phrase is not invented",
      not fid("We work on artificial intelligence tooling.",
              "We build AI tooling."),
      fid("We work on artificial intelligence tooling.", "We build AI tooling."))
check("fidelity: sentence-initial common word is not a name",
      not fid("The queries are slow and setup is long.",
              "Queries are slow. Setup is long."),
      fid("The queries are slow and setup is long.",
          "Queries are slow. Setup is long."))

# 12 — the region pass. hk and tw exist as separate languages precisely
# because these cases have to come out differently for each.
def region(text, lang):
    chk.sections.clear()
    chk.flags.clear()
    with redirect_stdout(io.StringIO()):
        chk.check_region(text, lang)
    return " | ".join(f["message"] for f in chk.flags)


# The premise: the same word is a defect on one side and native on the other.
_net = "我們的網絡團隊negotiated了新的軟件授權，項目下週上線。"
check("region: HK-native vocabulary flagged for Taiwan",
      "Hong Kong vocabulary" in region(_net, "tw"), region(_net, "tw"))
check("region: the same words pass as Hong Kong's own",
      "Hong Kong vocabulary" not in region(_net, "hk"), region(_net, "hk"))

_tw = "我們的網路團隊談好新的軟體授權，專案下週上線。"
check("region: TW-native vocabulary flagged for Hong Kong",
      "Taiwan vocabulary" in region(_tw, "hk"), region(_tw, "hk"))
check("region: the same words pass as Taiwan's own",
      "Taiwan vocabulary" not in region(_tw, "tw"), region(_tw, "tw"))

# Mainland-only vocabulary is wrong on both sides, so it must not be filed
# under either region's foreign list.
_ml = "這個視頻的質量不錯，信息也很完整。"
for _lang in ("hk", "tw"):
    check(f"region: mainland-only vocabulary flagged ({_lang})",
          "mainland" in region(_ml, _lang), region(_ml, _lang))

# Transliterations, the fastest tell.
check("region: TW transliteration flagged for Hong Kong",
      "transliteration" in region("川普訪問紐西蘭。", "hk"),
      region("川普訪問紐西蘭。", "hk"))
check("region: HK transliteration flagged for Taiwan",
      "transliteration" in region("特朗普訪問新西蘭。", "tw"),
      region("特朗普訪問新西蘭。", "tw"))

# Orthography: a partial conversion, and the one-to-many errors that survive
# it because every character involved is valid Traditional.
check("region: Simplified leakage flagged",
      "Simplified" in region("這個系統很复杂，需要时间。", "tw"),
      region("這個系統很复杂，需要时间。", "tw"))
check("region: one-to-many conversion error flagged",
      "conversion error" in region("最后我們把標准訂好了。", "tw"),
      region("最后我們把標准訂好了。", "tw"))
check("region: valid Traditional text raises no conversion error",
      "conversion error" not in region("最後我們把標準訂好了。", "tw"),
      region("最後我們把標準訂好了。", "tw"))

# 裡 / 裏 is one word with two regional standards.
check("region: 裡 flagged for Hong Kong",
      "裏" in region("在這裡工作。", "hk"), region("在這裡工作。", "hk"))
check("region: 裏 flagged for Taiwan",
      "裡" in region("在這裏工作。", "tw"), region("在這裏工作。", "tw"))
# The aspect particle forks; the bare character does not.
check("region: 著 particle flagged for Hong Kong",
      "接着" in region("接著我們開會。", "hk"), region("接著我們開會。", "hk"))
check("region: 着 particle flagged for Taiwan",
      "接著" in region("接着我們開會。", "tw"), region("接着我們開會。", "tw"))
check("region: 著作 and 顯著 are not flagged in Hong Kong text",
      not region("他的著作有顯著影響。", "hk"),
      region("他的著作有顯著影響。", "hk"))
check("region: pass does not run for zh, en or de",
      not region("这个视频的质量不错。", "zh"), region("这个视频的质量不错。", "zh"))

# Traditional text takes the CJK path for everything the zh mode already did.
_para = "系統支援批次處理。\n\n團隊花了兩週重寫排程。\n\n這週的數字回穩了。"
for _lang in ("hk", "tw"):
    _s = [s for p in chk.split_paragraphs(_para)
          for s in chk.split_sentences(p, _lang)]
    check(f"region: {_lang} splits sentences on 。like zh", len(_s) == 3, _s)
    check(f"region: {_lang} counts length in characters",
          chk.sentence_length("系統支援批次處理", _lang) == 8,
          chk.sentence_length("系統支援批次處理", _lang))

# Cantonese register detection must not fire on standard written Chinese that
# merely contains 係 or 仲. This was found by a rewrite being told its clean
# 書面語 was "mixed register" because it used the word 關係.
check("region: 關係 and 仲裁 are not Cantonese markers",
      chk.cantonese_hits("這與客戶關係和仲裁條款有關，仲介也一樣。") == 0,
      chk.cantonese_hits("這與客戶關係和仲裁條款有關，仲介也一樣。"))
check("region: real Cantonese still counts",
      chk.cantonese_hits("我哋係咁做嘅，佢唔知喺邊度。") >= 4,
      chk.cantonese_hits("我哋係咁做嘅，佢唔知喺邊度。"))

# 「」 is the standard on both sides; “” is the mainland convention.
_q, _ = scan("他說“這個做法不對”，然後就走了。", "tw")
check("region: “” flagged in Traditional text", "「」" in _q, _q)


# --- second-pass repairs -----------------------------------------------------
# Every case below is a defect two blind rewrite runs and a list audit found in
# the shipped version.

# A conversion artefact is reported as an objective error, so the sequence must
# not be matched across a word boundary. 17 of the 108 pairs used to fire on
# ordinary correct Traditional Chinese.
for _clean in ("抑制作用明顯", "體制造成問題", "舉手表決通過", "相關系統升級",
               "若干活動", "方面包括三項", "不只身高", "研發型企業",
               "上游行業", "牆面粉刷", "核准備查", "山谷物種", "民主干政",
               "太后來訪", "思維系統", "重複制定"):
    check(f"artifact: {_clean} is not a conversion error",
          not chk.artifact_hits(_clean), chk.artifact_hits(_clean))
for _bad in ("中國制造2025", "聯系我們", "標准化", "只身前往", "發型師",
             "上街游行", "以后再說", "雜志社"):
    check(f"artifact: {_bad} still is one", bool(chk.artifact_hits(_bad)))

# The name-fabrication gate did nothing at all for zh, hk and tw: names were
# only collected when the language was not CJK, so the pass printed clean
# unconditionally.
check("fidelity: invented Chinese organisation is caught",
      "明基電通公司" in fid("我們下週完成系統遷移。",
                            "明基電通公司下週完成系統遷移。", "tw"),
      fid("我們下週完成系統遷移。", "明基電通公司下週完成系統遷移。", "tw"))
check("fidelity: a shortened source name is not an invention",
      not fid("台灣觀光協會下週宣布。", "觀光協會下週宣布。", "tw"),
      fid("台灣觀光協會下週宣布。", "觀光協會下週宣布。", "tw"))
check("fidelity: ordinary Chinese prose invents nothing",
      not fid("本公司與該集團合作，本地區受影響。",
              "我們跟他們合作，這一區受影響。", "tw"),
      fid("本公司與該集團合作，本地區受影響。",
          "我們跟他們合作，這一區受影響。", "tw"))

# One attribution word anywhere in the rewrite used to switch the claim-theft
# check off for the whole document.
_src = "據業內專家表示，新版本效率提升了三成。我們下週上線。"
check("fidelity: a decoy attribution elsewhere does not disarm claim theft",
      "attributed claim" in fid(_src, "新版本效率提升了三成。理事長表示會如期上線。", "tw"),
      fid(_src, "新版本效率提升了三成。理事長表示會如期上線。", "tw"))
check("fidelity: keeping the attribution is still clean",
      not fid(_src, "有專家認為新版本效率提升了三成。理事長表示會如期上線。", "tw"))
check("fidelity: 整個 counts as raised severity",
      "整個" in fid("部分使用者受到影響。", "整個系統都掛了。", "tw"),
      fid("部分使用者受到影響。", "整個系統都掛了。", "tw"))

# 您 does not exist in Cantonese; 您好 is ordinary Taiwanese courtesy.
check("region: 您 is flagged for Hong Kong", "您" in region("感謝您的支持。", "hk"))
check("region: 您 is not flagged for Taiwan", "您" not in region("感謝您的支持。", "tw"))

# One-way glyph: 計畫 reads Taiwanese in HK prose, but Taiwanese writers use
# 計劃 freely, so the mirror rule would fire on ordinary Taiwanese writing.
check("region: 計畫 is flagged for Hong Kong", "計畫" in region("本計畫下月開始。", "hk"))
check("region: 計劃 is not flagged for Taiwan",
      "計畫" not in region("本計劃下月開始。", "tw"), region("本計劃下月開始。", "tw"))

# Set-phrase provenance: the nouns get converted and the skeleton does not.
check("region: Taiwan set-phrases are flagged in Hong Kong text",
      "set-phrase" in region("典禮圓滿落幕，多謝各界共襄盛舉。", "hk"),
      region("典禮圓滿落幕，多謝各界共襄盛舉。", "hk"))
check("region: Hong Kong correspondence is flagged in Taiwan text",
      "set-phrase" in region("是次會議謹此通知，順頌業祺。", "tw"),
      region("是次會議謹此通知，順頌業祺。", "tw"))
check("region: a region's own set-phrases are not called foreign",
      "set-phrase" not in region("典禮圓滿落幕，多謝各界共襄盛舉。", "tw"))

# Terms the catalogs call ordinary local writing must not fail the gate.
for _term, _lang in (("打造品牌是重點。", "tw"), ("解決管理痛點。", "tw"),
                     ("全方位服務。", "hk"), ("也因此我們改了做法。", "tw"),
                     ("設為唯讀模式。", "hk"), ("川貝燉雪梨。", "hk"),
                     ("推動健康城市計畫。", "tw"), ("宣布希望達成共識。", "hk")):
    _w, _ = scan(_term, _lang)
    check(f"gate: {_term} passes ({_lang})", not _w, _w)
check("region: 雪梨歌劇院 is still a Taiwan transliteration in HK text",
      "雪梨歌劇院" in region("雪梨歌劇院很有名。", "hk"))

# Taiwan's catalog revokes both of these; the checker used to enforce them.
_semi = "，".join(["系統支援批次處理；報表也能匯出"] * 6) + "。"
check("rhythm/punctuation: Taiwan is not failed for semicolons",
      "；" not in scan(_semi, "tw")[0], scan(_semi, "tw")[0])
check("punctuation: Hong Kong still is",
      "；" in scan(_semi, "hk")[0], scan(_semi, "hk")[0])

# Presence of 此外 is not a defect; a crowd of connectives is.
_crowd = ("此外，系統升級了。另一方面，效能提升。換言之，速度更快。"
          "更重要的是，成本下降。除此之外，介面重做。由此可見，值得投資。"
          "整體而言，這是好事。具體而言，三個模組都改了。")
check("vocabulary: a crowd of connectives is flagged",
      "connectives" in scan(_crowd, "tw")[0], scan(_crowd, "tw")[0])
check("vocabulary: one connective is not",
      "connectives" not in scan("此外，系統升級了。", "tw")[0])

check("vocabulary: Simplified Chinese has its own connective table",
      "connectives" in scan(
          "此外，系统升级了。另一方面，效能提升。换言之，速度更快。"
          "更重要的是，成本下降。除此之外，界面重做。由此可见，值得投资。", "zh")[0],
      scan("此外，系统升级了。另一方面，效能提升。换言之，速度更快。"
           "更重要的是，成本下降。除此之外，界面重做。由此可见，值得投资。", "zh")[0])

# Cantonese exceptions must all be honoured, not a hard-coded subset.
check("region: every CANTONESE_EXCEPTIONS entry is subtracted",
      chk.cantonese_hits("仲夏的昆仲關係，係屬重點解釋。") == 0,
      chk.cantonese_hits("仲夏的昆仲關係，係屬重點解釋。"))

# The two regions' set-phrase inventories must stay disjoint, or the cross-over
# would report a region's own formulas as the other region's.
check("lists: HK and TW set-phrases are disjoint",
      not (set(chk.HK_SET_PHRASES) & set(chk.TW_SET_PHRASES)),
      set(chk.HK_SET_PHRASES) & set(chk.TW_SET_PHRASES))
for _lang in ("hk", "tw"):
    _own = set(chk.VOCAB[_lang][1])
    _other = set(chk.REGION_FOREIGN_PHRASES[_lang])
    check(f"lists: {_lang} does not flag one phrase in two sections",
          not (_own & _other), _own & _other)


# Chinese prose writes quantities in Chinese numerals, so the figure check used
# to run on an empty set in any text without an ASCII digit.
check("fidelity: 兩點/三個 normalise against 2/3",
      not fid("遷移在凌晨兩點開始，用了三個星期。",
              "遷移在凌晨 2 點開始，用了 3 個星期。", "tw"),
      fid("遷移在凌晨兩點開始，用了三個星期。",
          "遷移在凌晨 2 點開始，用了 3 個星期。", "tw"))
check("fidelity: an invented Chinese-numeral figure is caught",
      "5" in fid("遷移涉及三個系統。", "遷移涉及五個系統。", "tw"),
      fid("遷移涉及三個系統。", "遷移涉及五個系統。", "tw"))
check("fidelity: 一 alone is not a figure",
      not fid("這一區受影響。", "這一區受到影響。", "tw"),
      fid("這一區受影響。", "這一區受到影響。", "tw"))

# Swapping a quantifier for its synonym is not an escalation.
check("fidelity: 所有 → 全部 is not raised severity",
      not fid("所有的社交軟件都刪掉。", "全部社交 app 都刪掉。", "tw"),
      fid("所有的社交軟件都刪掉。", "全部社交 app 都刪掉。", "tw"))
check("fidelity: 部分 → 所有人 still is",
      "所有人" in fid("部分使用者受到影響。", "所有人都受到影響。", "tw"),
      fid("部分使用者受到影響。", "所有人都受到影響。", "tw"))

# Cantonese grammar wearing standard characters — the defect a blind benchmark
# found and no character check can see.
_canto, _ = scan("團隊一樣處理到工作，服務維持正常。系統升級後反應更快。"
                 "我們會繼續改善。用戶不需要重新登入。", "hk")
check("region: 處理到 is flagged inside 書面語",
      "Cantonese syntax" in _canto, _canto)
_yue, _ = scan("我哋一樣處理到嘅工作，佢話冇問題㗎。系統升級咗之後快好多。"
               "我哋會繼續改善。用戶唔使重新登入。", "hk")
check("region: the same phrase is fine inside 粵文",
      "Cantonese syntax" not in _yue, _yue)

# Round-2 probes. Each of these was reported clean by the shipped checker
# while the catalog called it a defect.
check("region: mainland tech vocabulary from the new catalog rows is gated",
      all(w in region("新版數據看板上線，涉及三個模塊，響應速度提升，"
                      "運維團隊在移動端亦做了優化。", "hk")
          for w in ("模塊", "運維", "移動端")),
      region("新版數據看板上線，涉及三個模塊，響應速度提升，"
             "運維團隊在移動端亦做了優化。", "hk"))

_claim = "業內人士指出，這一輪的入職流程摩擦是最大的障礙。設定用了 45 分鐘。"
check("fidelity: claim theft survives a light rewrite",
      "attributed claim" in fid(
          _claim, "這個入職流程的摩擦才是最大的障礙。設定用了 45 分鐘。", "hk"),
      fid(_claim, "這個入職流程的摩擦才是最大的障礙。設定用了 45 分鐘。", "hk"))
check("fidelity: cutting the claim outright is still clean",
      not fid(_claim, "設定用了 45 分鐘，現在快了。", "hk"),
      fid(_claim, "設定用了 45 分鐘，現在快了。", "hk"))
check("fidelity: an adverb between subject and modal is still a promise",
      "first person" in fid("問題出在設定檔。",
                            "問題出在設定檔，我們下星期會修復。", "hk"),
      fid("問題出在設定檔。", "問題出在設定檔，我們下星期會修復。", "hk"))
check("fidelity: rewording 未來將 to 未來會 is not a new promise",
      not fid("未來將持續深化合作。", "未來會繼續跟他們合作。", "tw"),
      fid("未來將持續深化合作。", "未來會繼續跟他們合作。", "tw"))
check("fidelity: 部分 → 所有 is raised severity",
      "所有" in fid("部分用戶受到影響。", "所有用戶都受到影響。", "hk"),
      fid("部分用戶受到影響。", "所有用戶都受到影響。", "hk"))

check("fidelity: 依據 is not an attribution",
      not fid("本平台能依據使用者的偏好提供客製化行程。",
              "平台會依據使用者偏好安排行程。", "tw"),
      fid("本平台能依據使用者的偏好提供客製化行程。",
          "平台會依據使用者偏好安排行程。", "tw"))
check("fidelity: 據統計 still is",
      "attributed claim" in fid("據統計，超過八成用戶滿意這次改版。",
                                "超過八成用戶滿意這次改版。", "tw"),
      fid("據統計，超過八成用戶滿意這次改版。", "超過八成用戶滿意這次改版。", "tw"))

# 項目 is "item" in Taiwan, so the bare word cannot be gated — but 項目管理
# only ever means project management, and a Hong Kong announcement using it was
# otherwise mechanically indistinguishable from a Taiwanese one.
check("region: 項目管理 is flagged for Taiwan",
      "項目管理" in region("項目管理功能已重寫。", "tw"),
      region("項目管理功能已重寫。", "tw"))
check("region: bare 項目 is not",
      "項目" not in region("這次比賽項目有三個。", "tw"),
      region("這次比賽項目有三個。", "tw"))
check("region: 項目管理 is correct in Hong Kong text",
      "Taiwan vocabulary" not in region("項目管理功能已重寫。", "hk"),
      region("項目管理功能已重寫。", "hk"))

# 度身訂造 cannot be both H17's cliché and H1's prescribed replacement for
# 客製化. It was removed from the gate; the catalog now prescribes 自訂.
check("lists: 度身訂造 is not gated as a Hong Kong cliché",
      "度身訂造" not in chk.VOCAB["hk"][1])

# Batch convergence: five documents that each pass every single-document check
# while reading as one template. Two independent benchmark runs hit it.
import tempfile as _tf
with _tf.TemporaryDirectory() as _d:
    _dp = Path(_d)
    (_dp / "a.txt").write_text(
        "系統遷移在本星期六凌晨兩點開始，涉及三個核心系統。期間服務會受影響。"
        "請各組提前準備。", encoding="utf-8")
    (_dp / "b.txt").write_text(
        "系統遷移在本星期六凌晨兩點開始，涉及三個核心模組。期間服務會受影響。"
        "請各位提前準備。", encoding="utf-8")
    (_dp / "c.txt").write_text(
        "訂單系統下月改版。舊的匯出格式會保留到年底，之後停用。"
        "有疑問找我。", encoding="utf-8")
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_siblings([str(_dp / "a.txt"), str(_dp / "b.txt")], "hk")
    check("siblings: converged rewrites are flagged", _rc == 1, _buf.getvalue())
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_siblings([str(_dp / "a.txt"), str(_dp / "c.txt")], "hk")
    check("siblings: genuinely different rewrites are not",
          _rc == 0, _buf.getvalue())
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_siblings([str(_dp / "a.txt")], "hk")
    check("siblings: one file is a usage error", _rc == 2, _buf.getvalue())

# Two blind judges, from opposite sides, found the same defect: a Hong Kong and
# a Taiwanese rewrite of one source come out as one document in two accents.
# Every word differs, so no vocabulary check can see it.
with _tf.TemporaryDirectory() as _d:
    _dp = Path(_d)
    (_dp / "a.txt").write_text(
        "各位同事：\n\n今次遷移涉及三個系統。時間定於星期六凌晨。\n\n"
        "服務會受影響。不便之處，敬請見諒。\n\n多謝各位。\n\n有問題搵我。",
        encoding="utf-8")
    (_dp / "b.txt").write_text(
        "各位同事：\n\n這次搬遷動到三個系統。時間排在週六凌晨。\n\n"
        "服務會受影響。造成不便，還請多多包涵。\n\n謝謝大家。\n\n有問題找我。",
        encoding="utf-8")
    (_dp / "c.txt").write_text(
        "訂單系統下月改版。\n\n舊格式保留到年底。之後停用，不另行通知。"
        "要轉的話，後台自己可以改。\n\n有疑問找我。",
        encoding="utf-8")
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_siblings([str(_dp / "a.txt"), str(_dp / "b.txt")], "hk")
    check("siblings: one document in two accents is flagged",
          _rc == 1 and "two accents" in _buf.getvalue(), _buf.getvalue())
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_siblings([str(_dp / "a.txt"), str(_dp / "c.txt")], "hk")
    check("siblings: genuinely different documents are not",
          _rc == 0, _buf.getvalue())

# The genre gate. Three blind rounds failed on documents that stopped being the
# document they claimed to be, and nothing checked for it.
with _tf.TemporaryDirectory() as _d:
    _dp = Path(_d)
    (_dp / "ok.txt").write_text(
        "協作平台 3.0 今日推出，項目管理已重寫。詳情請瀏覽產品網站。",
        encoding="utf-8")
    (_dp / "gutted.txt").write_text(
        "項目管理已重寫，通知系統重構，反應速度有改善。", encoding="utf-8")
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_genre(str(_dp / "ok.txt"), "release", "hk")
    check("genre: a working release announcement passes", _rc == 0,
          _buf.getvalue())
    _buf = io.StringIO()
    with redirect_stdout(_buf):
        _rc = chk.run_genre(str(_dp / "gutted.txt"), "release", "hk")
    check("genre: one cut to a changelog does not", _rc == 1, _buf.getvalue())
    check("genre: it names what is missing rather than inventing it",
          "how to get it" in _buf.getvalue() and "fabrication" in _buf.getvalue(),
          _buf.getvalue())

# The catalogs name the terms that look gateable but must never be gated, so
# that a later editor who thinks "打造 is obviously AI slop, add it back" is
# contradicted by the file rather than by nobody. This test is the enforcement.
import re as _re


def _no_gate_terms(catalog):
    text = Path(catalog).read_text(encoding="utf-8")
    terms = []
    for m in _re.finditer(r"不可入閘[^\n]*?\*\*：([^\n]*)", text):
        body = m.group(1).split("——")[0]
        terms += [t.strip() for t in body.split("、") if t.strip()]
    return terms


for _skill, _lang in (("rewild-hk", "hk"), ("rewild-tw", "tw")):
    _catalog = ROOT / _skill / "references" / "patterns.md"
    _excluded = _no_gate_terms(_catalog)
    check(f"catalog: {_lang} declares its gate exclusions", len(_excluded) >= 8,
          _excluded)
    _gate = (set(chk.VOCAB[_lang][1]) | set(chk.REGION_FOREIGN[_lang])
             | set(chk.MAINLAND_ONLY) | set(chk.REGION_FOREIGN_PHRASES[_lang]))
    _leaked = sorted(set(_excluded) & _gate)
    check(f"catalog: no {_lang} gate-exclusion has crept into a gate list",
          not _leaked, _leaked)

# The pattern counts in the READMEs and on the landing page are a claim like
# any other, and they drifted three times while these catalogs were edited.
import re as _re2
_counts = {}
for _skill, _letter in (("rewild-hk", "H"), ("rewild-tw", "T")):
    _txt = (ROOT / _skill / "references" / "patterns.md").read_text(encoding="utf-8")
    _region = set(_re2.findall(rf"^#{{3,4}} ({_letter}\d+[a-z]?)\.", _txt, _re2.M))
    _c = set(_re2.findall(r"^### (C\d+)\.", _txt, _re2.M))
    _gen = {a or b for a, b in
            _re2.findall(r"^\*\*(\d+)\.|^### (\d+)\.", _txt, _re2.M)}
    _counts[_skill] = (len(_region) + len(_c) + len(_gen)
                       - len(_re2.findall(r"（已刪", _txt)))
_readme = (ROOT / "README.md").read_text(encoding="utf-8")
for _skill, _n in _counts.items():
    check(f"docs: README pattern count for {_skill} is {_n}",
          f"({_skill}/SKILL.md) | {_n} |" in _readme, _n)
_total = 46 + 45 + 48 + _counts["rewild-hk"] + _counts["rewild-tw"]
check(f"docs: README headline total is {_total}",
      f"**{_total} language-specific patterns." in _readme, _total)
check("docs: the landing page agrees with the README",
      f'<div class="stat-number">{_total}</div>'
      in (ROOT / "index.html").read_text(encoding="utf-8"), _total)

failed = [name for name, ok, _ in results if not ok]
print(f"\n{len(results) - len(failed)}/{len(results)} passed.")
sys.exit(1 if failed else 0)
