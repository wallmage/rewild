# Rewild

[![GitHub stars](https://img.shields.io/github/stars/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/watchers)
[![GitHub last commit](https://img.shields.io/github/last-commit/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild)
[![Top language](https://img.shields.io/github/languages/top/wallmage/rewild?style=flat-square)](https://github.com/wallmage/rewild)
[![Focus](https://img.shields.io/badge/focus-human%20writing-111827?style=flat-square)](https://github.com/wallmage/rewild)
[![Removes](https://img.shields.io/badge/removes-AI%20writing%20patterns-0f766e?style=flat-square)](https://github.com/wallmage/rewild)
[![Keeps](https://img.shields.io/badge/keeps-your%20voice-4f46e5?style=flat-square)](https://github.com/wallmage/rewild)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20%E7%B0%A1%20%7C%20%E6%B8%AF%20%7C%20%E5%8F%B0%20%7C%20DE-b45309?style=flat-square)](https://github.com/wallmage/rewild)
[![Blind A/B](https://img.shields.io/badge/blind%20A%2FB-83%25%20EN%20%C2%B7%2075%25%20ZH-2563eb?style=flat-square)](benchmarks/)
[![Region test](https://img.shields.io/badge/region%20attribution-50%2F50%20HK%20%C2%B7%20TW-16a34a?style=flat-square)](benchmarks/)
[![Editor review](https://img.shields.io/badge/native%20editor%20review-10%2F10%20HK%20%C2%B7%20TW-be123c?style=flat-square)](benchmarks/)

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體 · 香港](README.zh-HK.md) | [繁體 · 台灣](README.zh-TW.md) | [Deutsch](README.de.md)

AI text has a voice, and you've heard it. Inflated significance, adjective triplets, tidy summaries that say nothing. Most "humanizer" tools scrub all that off and hand back clean, flat prose. Rewild strips the patterns and puts your voice back: opinions, rhythm, rough edges. It won't invent facts or bolt on a personality that wasn't there.

**269 language-specific patterns. Five skills. A checker that reads your source, not just your draft.**

## Does it actually work?

Three things get measured, and they answer different questions.

**Is this version better than the last one?** Judges see both rewrites of the same text and have to pick one. No ties allowed, so the test can't saturate the way a checklist does. Five inputs, three independent judges, neither told which system wrote what.

| | English | Chinese |
|---|---|---|
| Preferred over the previous version | **10 / 12 (83%)** | **9 / 12 (75%)** |
| Reads less machine-written | yes | yes |

Chinese needed three rounds to get there: 6/12, then 7/12, then 9/12. Every round fixed a real defect. One example: four places in the Chinese skill treated sentence-final particles as a quota to hit, so the model bolted 啊 onto an internal email. All three judges rejected exactly that sentence. Particles are now a diagnosis, not a target.

**Does the Hong Kong text read as Hong Kong, and the Taiwan text as Taiwan?** This is the claim the Traditional Chinese skills actually make, so it gets tested directly. Three sources, three arms (`hk`, `tw`, and a generic "write like a human in Traditional Chinese" control), nine outputs blinded to single letters, three judges — one neutral, one reading as a Hong Kong reader, one as a Taiwanese reader.

| | result |
|---|---|
| Region attribution, skill outputs | **18 / 18** |
| Own-region naturalness ranking | **6 / 6** |

Every judge placed every text on the correct side — 50/50 across four rounds, including a second run that added the harder case the first one missed: a Taiwanese press release the Hong Kong skill has to convert, and a Hong Kong email the Taiwan skill has to convert. Nothing was mistaken for mainland writing. What makes the result mean something is that the control was not bad writing — judges called it fluent, and on vocabulary alone mostly Taiwanese, since an unguided model reaches for 專案 and 使用者 by default. What it could not do was commit: *"詞彙查對了台灣，但語感與收尾仍是大陸的."* One judge placed two of its three outputs in mainland China. Generic Traditional Chinese is a real output, and it belongs to nobody.

The run also found three defects, including one no tool can catch: 「處理到」 in a Hong Kong press release is Cantonese grammar wearing standard characters, invisible to a character-matching checker. All three are written up in [`benchmarks/`](benchmarks/).

**How good can one piece get?** The tests above are comparisons — this arm/that arm, which side does it land on. They stop telling you anything once both arms are correct, so there is a third measurement with no ceiling: hand one essay to a judge prompted entirely in Traditional Chinese as a thirty-year newspaper 副刊總編輯, have it score 1–10 and quote every line that reads machine-written, apply the fixes, resubmit.

| | Hong Kong | Taiwan |
|---|---|---|
| First draft | 5 | 5 |
| Seven rounds, fresh judge each round | 5 → 8 | 5 → 8 |
| Structural rewrite, one editor held across revisions | 7 → 8 → 9 | 8 → 9 |
| Final verdict | **10 — 落版，唔使再改** | **10 — 簽字發稿** |

**Vocabulary saturates; structure does not.** From round two on, neither editor could fault a single word — 「字係香港人嘅字，骨係機器嘅骨」 / 「字是台灣人的字，結構是機器的結構」. Everything between 8 and 10 was distribution, and it is now a pattern in all five catalogs (see *Why it works*). Same caveat as the region test: these judges are language models, not native readers. The protocol and the full trajectory are in [`benchmarks/`](benchmarks/).

**Is it better than a generic humanizer?** An older run scored 30/30 against a typical 24-rule tool's 24/30, and 30/30 against 20/30 in Chinese. Treat that number as unconfirmed: the raw outputs weren't kept, and the run predates the checker fixes below. The harness is in [`benchmarks/`](benchmarks/), with inputs, rubric, control prompt and blind-grading protocol, so you can rerun it and tell me I'm wrong.

> **Input:** In the rapidly evolving landscape of artificial intelligence, our company stands as a testament to innovation. Additionally, our groundbreaking platform provides a seamless, intuitive, and powerful experience.
>
> **Typical tool:** We built a platform that helps people get things done faster. Users seem to like it — early feedback suggests it saves real time on daily tasks.
>
> **Rewild:** We ship a product that saves people time. That's a fair claim. Calling it groundbreaking is the part that feels inflated.

The typical tool rewrites hype into quieter hype. Rewild names it.

## Why it works

Most humanizers run twenty-something generic rules. Remove "Additionally," vary sentence length, done. Enough to clear the obvious stuff and nothing more. The extra work here is in six places.

**Patterns per language, not one list for all of them.** English AI overuses "testament" and "landscape" and leans on em-dashes. Chinese AI drops modal particles and stacks four-character idioms. German AI avoids Modalpartikeln and splits compound words apart. Each language gets its own catalog, built from academic research and detection data — and for Traditional Chinese, per *region*, for the reason set out below.

**The tell that survives correct vocabulary.** Get every word right and a first-person piece still reads machine-made, because the craft is distributed too evenly: every paragraph lands a short dry close, every detail introduced gets paid off later, specifics are rationed one per paragraph, filler is sprinkled instead of clustered, and the closing image maps one-to-one onto the theme. Nothing is written badly, and that is the evidence. Swapping one perfect ending for a better one does not fix it — 「換衫，唔係換人」. The fix is to be willing to end flat, leave a detail unrecycled, and be vague everywhere except once. Every catalog carries it, and every `SKILL.md` carries the check: write out the last sentence of each paragraph and look at the column.

**Everyday register, not just press register.** The regional catalogs were strong on government, news and business Chinese and had nothing about a person describing their own phone — which is most of what anyone actually rewrites. They now carry it: 計數機/計算機/計算器, 碌/滑/刷手機, 讚好/按讚/點讚, 尿袋/行動電源/充電寶, and the platform-as-verb rows (WhatsApp 我 versus 賴我) that give away where a writer lives. Two native reviewers audited those rows and cut several. Each catalog now declares its own un-gateable list — Hong Kong: 平板, 封鎖, 應用程式, 截圖, 充電器, 計算器; Taiwan: 結帳, 追蹤, 動態, 平板, 截圖, 限時動態, 計算機 — words that read as ordinary on both sides, and a regression test enforces that none of them ever reaches a gate. Reverse-replacing a word that was already correct turns a region judgement into a register error, which reads worse than the problem it was fixing.

**A guard against overcorrecting.** Fix every text with the same three moves, punchy fragments and staged self-corrections and a rhetorical question per section, and you've built a new formula that reads just as machine-made as the old one. Rewild caps its interventions and rotates them.

**Fidelity, not just style.** This is the part most tools skip entirely. A rewrite can invent nothing on the usual list, no fake names and no fake numbers, and still end up saying something the source never said. Four ways that happens:

- The source credits a claim to someone; the rewrite drops the credit and keeps the claim
- The source describes; the rewrite promises
- The source says "impacted"; the rewrite says "nothing worked"
- The source names one cause; the rewrite rules others out

The bundled checker catches the first three by diffing your rewrite against your original. The fourth is on the writer, and the catalog says so.

**Nothing invented, including the modest-sounding things.** Every detail in the output has to exist in your source already. That rule used to have a hole in it: an older version told the model to replace deleted puffery with an honest, modest first-party claim, and it obliged. A marketing text grew a disclaimer nobody wrote. A release note had a company confess a weakness its own source never mentioned. A humble invention is still an invention.

## How it rewilds

For Hong Kong and Taiwan, one pass runs before any of this: a region scan over the whole text for the other region's vocabulary, its transliterations, mainland set-phrases and glyph errors. It comes first because region defects have nothing to do with whether a paragraph is clean — a paragraph with no AI tells at all can still be entirely the wrong side of the strait.

Then every paragraph gets sorted before anything is touched. Editing dense AI text line by line polishes the skeleton and leaves it standing, so the work splits three ways:

- **Already human?** Leave it. Over-editing is how these tools usually fail, so a clean paragraph gets nothing, or one small fix.
- **A few tells?** Fix them in place against the catalog.
- **Dense slop?** Re-say it. Note the facts, look away from the original, write it fresh in the same register, then check every fact back against the source.

Re-saying changes the wording, never the order. Moving an essay's stated most-important lesson to the end strands the setup that pointed at it.

Formal genres are exempt from re-saying altogether. Press releases, announcements and policy text get stripped and tightened instead, because their written skeleton *is* the register and re-saying slides into chat tone.

Two checks run before anything ships. A reviewer with no memory of the original reads the rewrite blind and flags what still sounds like AI. Then the checker measures what the model can't see in its own prose and compares the draft against the source. Style warnings are suggestions. Fidelity warnings are defects.

## Skills

| Skill | Patterns | What's unique |
|-------|----------|---------------|
| [English](rewild/SKILL.md) | 46 | Lean `SKILL.md` + detailed [pattern catalog](rewild/references/patterns.md) |
| [简体中文](rewild-zh/SKILL.md) | 45 | Mainland signals like 语气词缺失, 翻译腔, 四字套语, 公式化开头 |
| [繁體 · 香港](rewild-hk/SKILL.md) | 65 | 書面語/粵文 register branch, 「您」, 港式文言虛詞, 中英夾雜, 港式套語, 手機日常口語 |
| [繁體 · 台灣](rewild-tw/SKILL.md) | 65 | Japanese-derived structures protected as native, 台灣套語, 公文 skeleton, 港式書信骨架, 社群日常口語 |
| [Deutsch](rewild-de/SKILL.md) | 48 | German-specific signals like Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

Hong Kong and Taiwan are separate skills, not one Traditional Chinese skill with a region switch, and the reason is in the next section.

## Traditional Chinese is two languages here

The obvious design is one Traditional Chinese skill that takes a region flag. It cannot work, because **each region's native vocabulary overlaps the other's forbidden vocabulary.**

| | 香港 | 台灣 | 大陸 |
|---|---|---|---|
| software | 軟件 | 軟體 | 软件 |
| internet | 網絡 | 網路 | 网络 |
| smart | 智能 | 智慧 | 智能 |
| project | 項目 | 專案 | 项目 |
| Trump | 特朗普 | 川普 | 特朗普 |

Look at 網絡, 智能, 項目, 特朗普. Those are **mainland words a Taiwan skill must remove — and Hong Kong words a Hong Kong skill must protect.** One blocklist cannot hold both rules, and a region flag left unset makes the model average the two, producing exactly the text both audiences reject: correct Traditional Chinese that belongs to nobody.

Two more forks decide it. Transliterations are the fastest tell in the language — a Taiwanese reader hits 奧巴馬 and knows inside one sentence. And Hong Kong has a register axis Taiwan does not have at all: 書面語 versus 書面粵語 (係/唔/嘅/咗), a branch that would be dead weight in a Taiwan skill.

Neither catalog is a translation of the mainland one. All 45 mainland patterns were audited one at a time: Hong Kong keeps 29, adapts 15, deletes 1; Taiwan keeps 25, adapts 19, deletes 1. Both then add region patterns the mainland catalog never had — 21 for Hong Kong, 21 for Taiwan. Of 191 and 184 substantive paragraphs across the two files, exactly one is byte-identical. Some of the adaptations are *revocations* — rules that would flag ordinary local writing:

- 名詞化成癮 is deleted for Hong Kong. 作出／進行／予以 is HK written Chinese's most distinctive register marker, so a de-nominalising rule is the fastest way to sand off the voice.
- 功能詞失衡 is deleted for Taiwan. It came from an English corpus, and its "make sentences straighter" prescription fights Taiwan's natively looser register.
- Taiwan's Japanese-derived structures (「⋯的部分」「⋯性」「⋯感」) are marked native and protected. A mainland-tuned de-translationese rule strips them and pushes the text back toward mainland-neutral — the exact failure this skill exists to prevent.
- Hong Kong's emoji rule is relaxed, because HK institutional communication genuinely uses emoji on Facebook pages and WhatsApp notices.

Both catalogs end with a table of every revoked rule and why, so a future editor does not quietly reinstate one.

## How to use

1. Copy the skill folder for your language (`rewild/`, `rewild-zh/`, `rewild-hk/`, `rewild-tw/`, or `rewild-de/`) into your skills directory — for Claude Code that's `~/.claude/skills/`. Keep the folder name and contents as they are: the folder name matches the skill's own `name:` field, and the `references/` catalog and `scripts/` checker travel with it.
2. In any other LLM, paste `SKILL.md` as a system prompt and keep `references/patterns.md` on hand for the model to pull from.
3. Say "rewild this" and paste your text.

## The bundled checker

Every skill folder ships with [`scripts/naturalness-check.py`](rewild/scripts/naturalness-check.py), Python 3 with zero dependencies. Running it is a mandatory step in the workflow, not a nice-to-have.

Pass your original alongside your rewrite and it does both halves of the job:

```bash
python3 rewild/scripts/naturalness-check.py rewrite.txt --source original.txt --lang en
```

The style half measures what the catalogs describe: sentence-length uniformity, repeated openers, uniform paragraph sizes, AI vocabulary, connective density, punctuation problems. The fidelity half compares the two texts and flags invented names, invented figures, promises the original never made, stolen attributions and raised severity. In Chinese it reads names structurally (organisation, place and title-adjacent markers) and parses Chinese numerals, because a text that writes 三個星期 and 凌晨兩點 contains no ASCII digit and the figure check would otherwise run on nothing. It exits 1 while anything is flagged and 0 when clean, so it can gate a script.

For `--lang hk` and `--lang tw` there is a third half, which is the one the style checks are blind to. It flags the other region's vocabulary, mainland-only vocabulary, the other region's transliterations, Simplified characters that survived conversion, the regional glyph standards (裏/裡, 着/著, 身份/身分), and 您 in Hong Kong text — Cantonese has no such word, so one character places the source on the mainland.

It also checks the thing region conversion misses most often: **set phrases**. Converting a Hong Kong notice into Taiwanese finds four nouns to swap and leaves 是次、謹將⋯通知如下、鳴謝、順頌業祺 standing — correct Chinese, wrong bones. Which formulas count as provenance and which are merely common is decided by corpus counts, not by feel: 攜手合作 appears 74 times in 8.2M characters of Hong Kong government press releases, so it is a Taiwanese cliché but not evidence of a Taiwanese source, and it is excluded from that test.

It also catches a defect class no style checker looks for: **one-to-many conversion errors**. When Simplified converts to Traditional, one source character can map to several targets, and the converter picks wrong — 以后 for 以後, 標准 for 標準, 髮展 for 發展, 聯系 for 聯繫. Every character in those strings is valid Traditional Chinese. Only the meaning is wrong, which is why they survive proofreading.

Region warnings are defects, not suggestions. Style warnings are suggestions; a justified warning beats an unjustified edit.

There is one more mode, for the failure every per-document check is structurally blind to. Rewrite five related documents in one sitting and they converge — same paragraph count, same closing move, the same sentence carrying the same fact — while each one passes everything on its own:

```bash
python3 rewild-hk/scripts/naturalness-check.py --siblings out1.txt out2.txt out3.txt --lang hk
```

Two independent benchmark runs hit this and both had to catch it by reading the outputs side by side. Shared phrasing is expected when the sources genuinely overlap; a shared *shape* is a template wearing several coats of paint.

And one more, for the failure every blind round caught and no check looked for — a rewrite that is clean on region, register and fidelity while no longer being the document it claims to be:

```bash
python3 rewild-hk/scripts/naturalness-check.py rewrite.txt --genre outage --lang hk
```

`release`, `outage`, `pressrelease`, `notice`. It reports what is missing and refuses to help you fill it: if the source never carried a date or a contact, inventing one is fabrication, not repair.

One thing the checker does *not* do well, stated plainly: run it on a pattern catalog and it lights up, because catalogs quote wrong forms on purpose as teaching examples. It is built for rewrites. Use `--audit` on catalogs instead.

A few things it gets right that the obvious implementation doesn't. Markdown is read as prose rather than scaffolding. Headings, code fences and table rows are skipped, and list items count as their own sentences. Matching ignores typography, so `it's worth noting` is caught whichever apostrophe you typed. Vocabulary matches across inflections, so `streamline` also finds `streamlined` and `streamlining`. Abbreviations don't end sentences, which keeps `Dr. Chen shipped it at 4 p.m.` from counting as three.

Run `--audit` after editing a catalog. It compares the checker's word lists against the catalog beside it and names anything documented but invisible:

```bash
python3 rewild/scripts/naturalness-check.py --audit --lang en
```

Every bug the checker has ever shipped with is covered by a regression test — 146 of them now, up from 30:

```bash
python3 tests/test_checker.py
```

## Design

Each skill ships as two files plus a script, and the split is deliberate.

`SKILL.md` is the operating manual: when to fire, what to preserve, how to calibrate by genre, what voice actually sounds like. It loads into context every time, so it stays lean.

`references/patterns.md` is the diagnostic catalog: the full inventory of tells, with word lists, before/after pairs and citations. The model pulls in sections on demand rather than loading all of it upfront.

One thing that came out of testing, and it surprised me: where a rule sits matters as much as how it's worded. The fidelity rules originally sat at the end of the section about voice, so the last thing the model read before writing was a list of prohibitions. It wrote timidly and lost the blind comparison 5/12. Moving the identical text into a post-draft verification section took it to 10/12.

## Before / After

**AI-generated:**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it introduces batch processing, keyboard shortcuts, and offline mode, providing a seamless, intuitive, and powerful user experience.

**Rewilded:**
> The update adds batch processing, keyboard shortcuts, and offline mode — the three features that matter. Not a revolution. Just a good update that does what people actually asked for.

## Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) — 44-study synthesis
- KONVENS 2024 — German AI text detection
- De Gruyter 2025 — German linguistic complexity analysis
- Huxiu quantitative analysis — Chinese rhetorical device frequencies
- AIGCleaner — Chinese detection weights
- 教育部《兩岸常用詞典》 — cross-strait lexicon, including its 港澳 column
- 香港《政府公文寫作手冊》 (3rd ed.) and 邵敬敏〈香港詞語的特點〉 — HK register and the AB/BA reversal set
- 台灣《法律統一用字表》 and 《常用字字形表》 — the 布/佈 and 裡/裏 standards
- 2,934 Hong Kong government press releases (info.gov.hk, May–July 2026, 8.2M characters) — frequency evidence for the 港式套語 list, and for which cross-strait formulas are *not* provenance signals

## Shipping notes

- Fires only when you say the problem is AI-sounding text
- Adds no metric, anecdote or experience your source didn't have
- Keeps formal writing formal
- Builds voice from details already in your text
- Blind-reviews every rewrite before delivery, and diffs it against your source
- For Hong Kong and Taiwan, treats wrong-region vocabulary as a defect rather than a style preference

---

## Author

[Wallny](https://github.com/wallmage)
