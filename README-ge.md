# Rewild

KI-Schreibmuster aus Text entfernen. Damit es klingt, als hätte ein Mensch geschrieben — weil du es warst.

**3 Sprachen, 50+ Erkennungsmuster.**

| Skill | Muster | Besonderheit |
|-------|--------|--------------|
| [English](rewild-en/SKILL.md) | 40 | Vollständiges Musterset basierend auf Wikipedia + 2025-2026 Forschung |
| [中文](rewild-zh/SKILL.md) | 46 | 10 chinesisch-spezifische Muster |
| [Deutsch](rewild-ge/SKILL.md) | 37 | 13 deutsch-spezifische Muster: Modalpartikeln, Komposita, Geviertstrich, Nebensatz, Konjunktiv |

## So funktioniert's

1. Kopiere die `SKILL.md` für deine Sprache
2. Füge sie als Skill in Claude Code / Cowork ein, oder als System Prompt in einem beliebigen LLM-Tool
3. Sag "rewild das" und füg deinen Text ein

## Vorher / Nachher

**KI-generiert:**
> In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen. Darüber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung. Zusammenfassend lässt sich sagen, dass die Zukunft vielversprechend aussieht.

**Nach Rewild:**
> Ich hab letzte Woche ChatGPT unsere Quartalszahlen zusammenfassen lassen. Das Ergebnis klang wie eine Laudatio auf eine Firma, die's gar nicht gibt. Mein Chef hat gelacht. "Schreib's halt selber", hat er gesagt.

## Deutsch-spezifische Muster

Rewild-GE erkennt 13 Muster, die nur im Deutschen auftreten:

- **Modalpartikeln fehlen** — doch/halt/mal/eben/ja sind die Seele der deutschen Sprache; KI nutzt sie kaum
- **Geviertstrich statt Halbgeviertstrich** — Englischer em dash (—) statt korrektem deutschen en dash (–)
- **Falsche Anführungszeichen** — Englische "..." statt deutschen ,,..."
- **Nebensatz-Wortstellung** — Verb nicht am Ende des Nebensatzes
- **Komposita zerlegt** — "Taschen-Rechner" statt Taschenrechner
- **Konnektoren-Flut** — "Darüber hinaus" / "Zusammenfassend lässt sich sagen"
- **Formelhafte Eröffnungen** — "In der heutigen Zeit..." = sofortiger KI-Marker
- **Kasus-Hyperkorrektheit** — Überformaler Genitiv wo Dativ natürlicher wäre
- **Passiv-Ketten** — Drei Passivsätze hintereinander + Nominalstil
- **Konjunktiv-Übernutzung** — "könnte/würde/sollte" überall
- **Wörtliche Übersetzungen** — "Sie nahm einen tiefen Atemzug" statt "Sie atmete tief durch"
- **Fehlende regionale Färbung** — Kein Österreichisch, Schweizerdeutsch oder Dialekt
- **Orthographische Inkonsistenz** — Verschiedene Schreibweisen im selben Text

## Quellen

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- ADVERTEXT Lektoratstest
- Kathrin Landsdorfer — 21 ChatGPT-Phrasen
- ContentConsultants, WORTLIGA, fyrfeed
- KONVENS 2024 (Irrgang et al.)
- De Gruyter 2025 — Linguistische Komplexitätsanalyse

---

**[English](README.md)** | **[中文说明](README-zh.md)**

## Autor

[Wallny](https://github.com/wallmage)
