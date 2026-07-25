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
[![Languages](https://img.shields.io/badge/languages-English%20%7C%20%E4%B8%AD%E6%96%87%20%7C%20Deutsch-b45309?style=flat-square)](https://github.com/wallmage/rewild)
[![Blind A/B](https://img.shields.io/badge/blind%20A%2FB-83%25%20EN%20%C2%B7%2075%25%20ZH-2563eb?style=flat-square)](benchmarks/)

[English](README.md) | [中文](README.zh-CN.md) | [Deutsch](README.de.md)

AI text has a voice, and you've heard it. Inflated significance, adjective triplets, tidy summaries that say nothing. Most "humanizer" tools scrub all that off and hand back clean, flat prose. Rewild strips the patterns and puts your voice back: opinions, rhythm, rough edges. It won't invent facts or bolt on a personality that wasn't there.

**139 language-specific patterns. Three languages. A checker that reads your source, not just your draft.**

## Does it actually work?

Two things get measured, and they answer different questions.

**Is this version better than the last one?** Judges see both rewrites of the same text and have to pick one. No ties allowed, so the test can't saturate the way a checklist does. Five inputs, three independent judges, neither told which system wrote what.

| | English | Chinese |
|---|---|---|
| Preferred over the previous version | **10 / 12 (83%)** | **9 / 12 (75%)** |
| Reads less machine-written | yes | yes |

Chinese needed three rounds to get there: 6/12, then 7/12, then 9/12. Every round fixed a real defect. One example: four places in the Chinese skill treated sentence-final particles as a quota to hit, so the model bolted 啊 onto an internal email. All three judges rejected exactly that sentence. Particles are now a diagnosis, not a target.

**Is it better than a generic humanizer?** An older run scored 30/30 against a typical 24-rule tool's 24/30, and 30/30 against 20/30 in Chinese. Treat that number as unconfirmed: the raw outputs weren't kept, and the run predates the checker fixes below. The harness is in [`benchmarks/`](benchmarks/), with inputs, rubric, control prompt and blind-grading protocol, so you can rerun it and tell me I'm wrong.

> **Input:** In the rapidly evolving landscape of artificial intelligence, our company stands as a testament to innovation. Additionally, our groundbreaking platform provides a seamless, intuitive, and powerful experience.
>
> **Typical tool:** We built a platform that helps people get things done faster. Users seem to like it — early feedback suggests it saves real time on daily tasks.
>
> **Rewild:** We ship a product that saves people time. That's a fair claim. Calling it groundbreaking is the part that feels inflated.

The typical tool rewrites hype into quieter hype. Rewild names it.

## Why it works

Most humanizers run twenty-something generic rules. Remove "Additionally," vary sentence length, done. Enough to clear the obvious stuff and nothing more. The extra work here is in four places.

**Patterns per language, not one list for all of them.** English AI overuses "testament" and "landscape" and leans on em-dashes. Chinese AI drops modal particles and stacks four-character idioms. German AI avoids Modalpartikeln and splits compound words apart. Each language gets its own catalog, built from academic research and detection data.

**A guard against overcorrecting.** Fix every text with the same three moves, punchy fragments and staged self-corrections and a rhetorical question per section, and you've built a new formula that reads just as machine-made as the old one. Rewild caps its interventions and rotates them.

**Fidelity, not just style.** This is the part most tools skip entirely. A rewrite can invent nothing on the usual list, no fake names and no fake numbers, and still end up saying something the source never said. Four ways that happens:

- The source credits a claim to someone; the rewrite drops the credit and keeps the claim
- The source describes; the rewrite promises
- The source says "impacted"; the rewrite says "nothing worked"
- The source names one cause; the rewrite rules others out

The bundled checker catches the first three by diffing your rewrite against your original. The fourth is on the writer, and the catalog says so.

**Nothing invented, including the modest-sounding things.** Every detail in the output has to exist in your source already. That rule used to have a hole in it: an older version told the model to replace deleted puffery with an honest, modest first-party claim, and it obliged. A marketing text grew a disclaimer nobody wrote. A release note had a company confess a weakness its own source never mentioned. A humble invention is still an invention.

## How it rewilds

Every paragraph gets sorted before anything is touched. Editing dense AI text line by line polishes the skeleton and leaves it standing, so the work splits three ways:

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
| [中文](rewild-zh/SKILL.md) | 45 | Chinese-specific signals like 语气词缺失, 翻译腔, 四字套语, 公式化开头 |
| [Deutsch](rewild-de/SKILL.md) | 48 | German-specific signals like Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## How to use

1. Copy the skill folder for your language (`rewild/`, `rewild-zh/`, or `rewild-de/`) into your skills directory — for Claude Code that's `~/.claude/skills/`. Keep the folder name and contents as they are: the folder name matches the skill's own `name:` field, and the `references/` catalog and `scripts/` checker travel with it.
2. In any other LLM, paste `SKILL.md` as a system prompt and keep `references/patterns.md` on hand for the model to pull from.
3. Say "rewild this" and paste your text.

## The bundled checker

Every skill folder ships with [`scripts/naturalness-check.py`](rewild/scripts/naturalness-check.py), Python 3 with zero dependencies. Running it is a mandatory step in the workflow, not a nice-to-have.

Pass your original alongside your rewrite and it does both halves of the job:

```bash
python3 rewild/scripts/naturalness-check.py rewrite.txt --source original.txt --lang en
```

The style half measures what the catalogs describe: sentence-length uniformity, repeated openers, uniform paragraph sizes, AI vocabulary, punctuation problems. The fidelity half compares the two texts and flags names, figures, promises, stolen attributions and raised severity. It exits 1 while anything is flagged and 0 when clean, so it can gate a script.

A few things it gets right that the obvious implementation doesn't. Markdown is read as prose rather than scaffolding. Headings, code fences and table rows are skipped, and list items count as their own sentences. Matching ignores typography, so `it's worth noting` is caught whichever apostrophe you typed. Vocabulary matches across inflections, so `streamline` also finds `streamlined` and `streamlining`. Abbreviations don't end sentences, which keeps `Dr. Chen shipped it at 4 p.m.` from counting as three.

Run `--audit` after editing a catalog. It compares the checker's word lists against the catalog beside it and names anything documented but invisible:

```bash
python3 rewild/scripts/naturalness-check.py --audit --lang en
```

Thirty regression tests cover every bug the checker has ever shipped with:

```bash
python3 tests/test_checker.py
```

## Design

Each language ships as two files, and the split is deliberate.

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

## Shipping notes

- Fires only when you say the problem is AI-sounding text
- Adds no metric, anecdote or experience your source didn't have
- Keeps formal writing formal
- Builds voice from details already in your text
- Blind-reviews every rewrite before delivery, and diffs it against your source

---

## Author

[Wallny](https://github.com/wallmage)
