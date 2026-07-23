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
[![Benchmark](https://img.shields.io/badge/benchmark-30%2F30-2563eb?style=flat-square)](https://github.com/wallmage/rewild)

[English](README.md) | [中文](README.zh-CN.md) | [Deutsch](README.de.md)

AI text has a voice. You've heard it: the inflated significance, the adjective triplets, the tidy summaries that say nothing. Most "humanizer" tools just scrub that away and leave you with clean, flat text. Rewild strips the AI patterns and puts *your* voice back — opinions, rhythm, rough edges and all. It won't invent facts or bolt on a fake personality.

**30/30 benchmark. 40+ language-specific patterns. Three languages.**

## Benchmark: Rewild vs. a typical humanizer

Same AI text, same model, blind comparison. 10 assertions per output, 3 test prompts.

| | Rewild | Typical 24-pattern tool |
|---|---|---|
| **Score** | **30 / 30 (100%)** | 24 / 30 (80%) |
| No AI vocabulary | 6/6 | 6/6 |
| No meta-commentary | 6/6 | 5/6 |
| Sentence length variety | 6/6 | 4/6 |
| Adds specific details | 6/6 | 4/6 |
| Shows opinion/emotion | 6/6 | 5/6 |

The first three rows are basically tied — any decent tool can strip AI slop. The gap is in the last two: adding real detail and showing a point of view. A typical humanizer stops at removal. Clean text, no soul. Rewild scores 30/30 because "not sounding like AI" is the floor, not the goal. It pulls real details out of your source and lets the text actually say something.

**Chinese benchmark:** The gap is even wider — **30/30 (100%)** vs. **20/30 (67%)**. Generic tools have zero Chinese-specific patterns. They miss modal particle absence (语气词), idiom stacking (四字套语), and translation-ese (翻译腔) — the three strongest Chinese AI tells.

> **Input:** In the rapidly evolving landscape of artificial intelligence, our company stands as a testament to innovation. Additionally, our groundbreaking platform provides a seamless, intuitive, and powerful experience — ensuring that users can accomplish their goals efficiently.
>
> **Typical tool:** We built a platform that helps people get things done faster. Users seem to like it -- early feedback suggests it saves real time on daily tasks. Whether that holds up as we scale is an honest question.
>
> **Rewild:** We ship a product that saves people time. That's a fair claim. Calling it groundbreaking and industry-changing is the part that feels inflated.

The typical tool rewrites the hype into different hype. Rewild calls the hype what it is.

## Why Rewild works

Most humanizers run 20-something generic rules: remove "Additionally," vary sentence length, done. That gets you past the obvious stuff. Rewild does more, and the extra work falls into four buckets:

**40+ language-specific patterns, not 20 generic ones.** Each language has its own AI tells. English AI overuses "testament," "landscape," and em-dashes. Chinese AI drops modal particles and stacks four-character idioms. German AI avoids Modalpartikeln and breaks apart compound words. Each language gets its own pattern catalog, sourced from academic research and real detection data.

**An overcorrection guard.** Humanizers that fix every text with the same three moves — punchy fragments, staged self-corrections, rhetorical questions — just produce a new, equally recognizable formula. Rewild caps its own interventions and rotates them, so ten rewrites don't converge on one voice.

**Two-layer architecture.** A lean `SKILL.md` (the operating manual) loads fast and sets the rules. A deep `references/patterns.md` (the diagnostic catalog) loads on demand when the model needs specifics — word lists, before/after examples, academic citations. You get precision without burning your whole context window on startup.

**Anti-fabrication as a core rule.** Most tools "humanize" by inventing anecdotes, fake metrics, or first-person experiences. Rewild won't. Every detail in the output has to already exist in your source text. Voice comes from rhythm and opinion, not from making things up.

## How it rewilds

Rewild sorts each paragraph before touching it. Editing dense AI text line by line just polishes the skeleton and leaves it standing, so the workflow splits the job three ways:

- **Already human?** Leave it. Over-editing is the most common way these tools fail — a clean paragraph gets nothing, or one small fix.
- **A few tells?** Fix them in place against the pattern catalog.
- **Dense slop?** Re-say it. Note the facts, look away from the original, write the paragraph fresh in the same register, then check every fact back against the source.

Formal genres are the exception. Press releases, announcements, and policy text get stripped and tightened, never fully re-said — their written skeleton *is* the register, and re-saying slides into chat tone. Full re-saying is for essays and posts, where the voice carries the piece.

Two checks run before delivery. A clean-context reviewer reads the rewrite blind and flags whatever still sounds like AI. Then the bundled checker measures the statistical tells the model can't spot in its own prose, and the draft gets fixed until it comes back clean. This workflow is blind-tested: an earlier version's outputs were graded against the current one by judges that didn't know which was which, and the current workflow won every test.

## Skills

| Skill | Patterns | What's unique |
|-------|----------|---------------|
| [English](rewild-en/SKILL.md) | 42 | Lean `SKILL.md` + detailed [pattern catalog](rewild-en/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 41 | Chinese-specific signals like 语气词缺失, 翻译腔, 四字套语, 公式化开头 |
| [Deutsch](rewild-de/SKILL.md) | 42 | German-specific signals like Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## How to use

1. Copy the skill folder for your language (`rewild-en/` or `rewild-zh/`) into your skills directory — for Claude Code that's `~/.claude/skills/`. Keep the folder intact: the `references/` catalog and `scripts/` checker travel with it.
2. Or, in any other LLM, paste the `SKILL.md` as a system prompt and keep `references/patterns.md` on hand for the model to pull from.
3. Say "rewild this" and paste your text.

## Automatic naturalness check

Every skill folder ships with [`scripts/naturalness-check.py`](rewild-en/scripts/naturalness-check.py) (Python 3, zero dependencies). It measures the statistical tells the catalogs describe: sentence-length uniformity, repeated sentence openers, uniform paragraph sizes, AI vocabulary, and punctuation problems (em-dash density, quote-style mixing, half-width marks in Chinese, missing `–` in German).

Running it is a mandatory step in the workflow: the model checks every rewrite and fixes warnings until the report is clean before delivering. You can also run it by hand on any text:

```
python3 rewild-en/scripts/naturalness-check.py draft.txt --lang en
```

## Design

Each language ships as two files. The split is deliberate.

`SKILL.md` is the operating manual — when to fire, what to preserve, genre calibration, what voice sounds like. Quick-reference checklist, worked example, scoring rubric. Loads into context every time.

`references/patterns.md` is the diagnostic catalog. Full inventory of language-specific AI tells: word lists, before/after examples, severity rankings, academic citations. The model pulls in sections on demand instead of loading everything upfront.

Fast startup, deep diagnostics when you need them, no wasted context.

## Before / After

**AI-generated:**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it introduces batch processing, keyboard shortcuts, and offline mode, providing a seamless, intuitive, and powerful user experience — ensuring that users can accomplish their goals efficiently.

**Rewilded:**
> The update adds batch processing, keyboard shortcuts, and offline mode — the three features that matter. Not a revolution. Just a good update that does what people actually asked for.

## Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) — 44-study synthesis
- KONVENS 2024 — German AI text detection
- De Gruyter 2025 — German linguistic complexity analysis
- Huxiu quantitative analysis — Chinese rhetorical device frequencies
- AIGCleaner — Chinese detection weights

## Shipping Notes

- Tight trigger: only fires when you explicitly say "this sounds like AI"
- Anti-fabrication: no invented metrics, anecdotes, or experiences
- Genre-aware: formal writing stays formal
- Source-grounded: adds voice by pulling forward real details, not inventing new ones
- Two-pass by default: a clean-context subagent blind-reviews every rewrite before delivery

---

## Author

[Wallny](https://github.com/wallmage)
