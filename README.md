# Rewild

Remove AI writing patterns from text. Make it sound like a human wrote it — because you did.

**50+ detection patterns across 3 languages.**

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

**Why the gap?** Both tools strip AI slop equally well. The difference is what happens next. A typical humanizer stops at removal and leaves clean but soulless text. Rewild's 16 additional patterns — backed by 8 academic sources — teach the model what human writing actually *sounds* like: rhythm variation, concrete specifics, self-correction, sensory language, and surprising word choices.

> **Input:** In the rapidly evolving landscape of artificial intelligence, our company stands as a testament to innovation. Additionally, our groundbreaking platform provides a seamless, intuitive, and powerful experience — ensuring that users can accomplish their goals efficiently.
>
> **Typical tool:** We built a platform that helps people get things done faster. Users seem to like it -- early feedback suggests it saves real time on daily tasks. Whether that holds up as we scale is an honest question.
>
> **Rewild:** We ship a product that saves people time. The platform is fast to learn and gets out of your way -- which, after years of bloated enterprise tools, feels almost radical. Is it going to reshape the entire industry? I have no idea. But two Fortune 500 companies switched to us last quarter, and their ops teams cut reporting time by 30%.

## Skills

| Skill | Patterns | What's unique |
|-------|----------|---------------|
| [English](rewild-en/SKILL.md) | 40 | Full pattern set based on Wikipedia + 2025-2026 academic research |
| [中文](rewild-zh/SKILL.md) | 46 | 10 Chinese-specific: 语气词缺失, 四字成语堆砌, 翻译腔, 公式化开头 |
| [Deutsch](rewild-ge/SKILL.md) | 37 | 13 German-specific: Modalpartikeln, Komposita, Geviertstrich, Nebensatz, Konjunktiv |

## How to use

1. Copy the `SKILL.md` for your language
2. Add it as a skill in Claude Code / Cowork, or paste as a system prompt in any LLM
3. Say "rewild this" and paste your text

## Before / After

**AI-generated:**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience — ensuring that users can accomplish their goals efficiently.

**Rewilded:**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

## Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) — 44-study synthesis
- KONVENS 2024 — German AI text detection
- De Gruyter 2025 — German linguistic complexity analysis
- Huxiu quantitative analysis — Chinese rhetorical device frequencies
- AIGCleaner — Chinese detection weights

---

**[中文说明](README-zh.md)** | **[Deutsche Anleitung](README-ge.md)**

## Author

[Wallny](https://github.com/wallmage)
