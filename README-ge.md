# Rewild

KI-Schreibmuster aus Text entfernen. Damit es klingt, als haette ein Mensch geschrieben — weil du es warst.

**3 Sprachen, 50+ Erkennungsmuster.**

| Skill | Muster | Besonderheit |
|-------|--------|--------------|
| [English](rewild-en/SKILL.md) | 40 | Vollstaendiges Musterset basierend auf Wikipedia + 2025-2026 Forschung |
| [中文](rewild-zh/SKILL.md) | 46 | 10 chinesisch-spezifische Muster |
| [Deutsch](rewild-ge/SKILL.md) | 37 | 13 deutsch-spezifische Muster: Modalpartikeln, Komposita, Geviertstrich, Nebensatz, Konjunktiv |

## So funktioniert's

1. Kopiere die `SKILL.md` fuer deine Sprache
2. Fuege sie als Skill in Claude Code / Cowork ein, oder als System Prompt in einem beliebigen LLM-Tool
3. Sag "rewild das" und fueg deinen Text ein

## Vorher / Nachher

**KI-generiert:**
> In der heutigen Zeit ist es wichtiger denn je, sich mit kuenstlicher Intelligenz auseinanderzusetzen. Darueber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung. Zusammenfassend laesst sich sagen, dass die Zukunft vielversprechend aussieht.

**Nach Rewild:**
> Ich hab letzte Woche ChatGPT unsere Quartalszahlen zusammenfassen lassen. Das Ergebnis klang wie eine Laudatio auf eine Firma, die's gar nicht gibt. Mein Chef hat gelacht. "Schreib's halt selber", hat er gesagt.

## Deutsch-spezifische Muster

Rewild-GE erkennt 13 Muster, die nur im Deutschen auftreten:

- **Modalpartikeln fehlen** — doch/halt/mal/eben/ja sind die Seele der deutschen Sprache; KI nutzt sie kaum
- **Geviertstrich statt Halbgeviertstrich** — Englischer em dash (—) statt korrektem deutschen en dash (–)
- **Falsche Anfuehrungszeichen** — Englische "..." statt deutschen ,,..."
- **Nebensatz-Wortstellung** — Verb nicht am Ende des Nebensatzes
- **Komposita zerlegt** — "Taschen-Rechner" statt Taschenrechner
- **Konnektoren-Flut** — "Darueber hinaus" / "Zusammenfassend laesst sich sagen"
- **Formelhafte Eroeffnungen** — "In der heutigen Zeit..." = sofortiger KI-Marker
- **Kasus-Hyperkorrektheit** — Ueberformaler Genitiv wo Dativ natuerlicher waere
- **Passiv-Ketten** — Drei Passivsaetze hintereinander + Nominalstil
- **Konjunktiv-Uebernutzung** — "koennte/wuerde/sollte" ueberall
- **Woertliche Uebersetzungen** — "Sie nahm einen tiefen Atemzug" statt "Sie atmete tief durch"
- **Fehlende regionale Faerbung** — Kein Oesterreichisch, Schweizerdeutsch oder Dialekt
- **Orthographische Inkonsistenz** — Verschiedene Schreibweisen im selben Text

## Quellen

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- ADVERTEXT Lektoratstest
- Kathrin Landsdorfer — 21 ChatGPT-Phrasen
- ContentConsultants, WORTLIGA, fyrfeed
- KONVENS 2024 (Irrgang et al.)
- De Gruyter 2025 — Linguistische Komplexitaetsanalyse

---

**[English](README.md)** | **[中文说明](README-zh.md)**

## Autor

[Wallny](https://github.com/wallmage)
