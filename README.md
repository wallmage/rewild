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

Remove AI writing patterns from text. Make it sound like a human wrote it — because you did.

**3 languages. Lean skills, detail catalogs on demand.**

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

**Why the gap?** Both tools strip AI slop equally well. A typical humanizer stops at removal — clean text, no soul. Rewild cleans AI patterns without inventing new facts or faking specificity.

**Chinese benchmark:** The gap is wider here — **30/30 (100%)** vs. **20/30 (67%)**. A generic tool has no Chinese-specific patterns, so it misses modal particle absence (语气词), idiom stacking, and translation-ese. Those are the strongest Chinese AI tells.

> **Input:** In the rapidly evolving landscape of artificial intelligence, our company stands as a testament to innovation. Additionally, our groundbreaking platform provides a seamless, intuitive, and powerful experience — ensuring that users can accomplish their goals efficiently.
>
> **Typical tool:** We built a platform that helps people get things done faster. Users seem to like it -- early feedback suggests it saves real time on daily tasks. Whether that holds up as we scale is an honest question.
>
> **Rewild:** We ship a product that saves people time. That's a fair claim. Calling it groundbreaking and industry-changing is the part that feels inflated.

## Skills

| Skill | Patterns | What's unique |
|-------|----------|---------------|
| [English](rewild-en/SKILL.md) | 40 | Lean `SKILL.md` + detailed [pattern catalog](rewild-en/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 40 | Chinese-specific signals like 语气词缺失, 翻译腔, 四字套语, 公式化开头 |
| [Deutsch](rewild-de/SKILL.md) | 41 | German-specific signals like Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## How to use

1. Copy the `SKILL.md` for your language
2. Add it as a skill in Claude Code / Cowork, or paste as a system prompt in any LLM
3. Keep the matching `references/patterns.md` beside it so the model can load details on demand
4. Say "rewild this" and paste your text

## Design

Each language ships in two layers:

- `SKILL.md`: operating manual — trigger scope, core rules, soul guidance, genre calibration, worked example, scoring rubric
- `references/patterns.md`: diagnostic catalog — language-specific AI tells, word lists, before/after examples, academic citations

The skill loads fast. The catalog loads on demand.

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

---

## Author

[Wallny](https://github.com/wallmage)
