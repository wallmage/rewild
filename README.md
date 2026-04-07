# Rewild

Remove AI writing patterns from text. Make it sound like a human wrote it — because you did.

**50+ detection patterns across 3 languages.**

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
