# Rewild

[English](README.md) | [中文](README.zh-CN.md) | [Deutsch](README.de.md)

KI-Schreibmuster aus Text entfernen. Damit es klingt, als hätte ein Mensch geschrieben — weil du es warst.

**3 Sprachen. Schlanke Skills. Musterkataloge bei Bedarf.**

## Benchmark: Rewild vs. ein typisches Humanizer-Tool

Gleicher KI-Text, gleiches Modell, Blindvergleich. 10 Kriterien pro Ausgabe, 3 Testprompts.

| | Rewild | Typisches 24-Muster-Tool |
|---|---|---|
| **Ergebnis** | **30 / 30 (100%)** | 24 / 30 (80%) |
| Kein KI-Vokabular | 6/6 | 6/6 |
| Kein Meta-Kommentar | 6/6 | 5/6 |
| Satzlängen-Variation | 6/6 | 4/6 |
| Konkrete Details ergänzt | 6/6 | 4/6 |
| Zeigt Meinung/Emotion | 6/6 | 5/6 |

**Warum der Unterschied?** Beide Tools entfernen KI-Muster gleich gut. Der Unterschied liegt danach. Ein typisches Tool hört beim Entfernen auf – sauberer, aber seelenloser Text bleibt übrig. Rewild ist jetzt außerdem strenger darin, keine neuen Fakten, Anekdoten oder falsche Konkretheit zu erfinden.

**Chinesisch-Benchmark:** Der Abstand ist noch größer — **30/30 (100%)** vs. **20/30 (67%)**. Ein generisches Tool hat null chinesisch-spezifische Muster und erkennt daher keine fehlenden Modalpartikeln (语气词), keine Idiom-Häufungen oder Übersetzungs-Stil.

## Skills

| Skill | Muster | Besonderheit |
|-------|--------|--------------|
| [English](rewild-en/SKILL.md) | 40 | Schlankes `SKILL.md` + ausführlicher [pattern catalog](rewild-en/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 40 | Chinesisch-spezifische Muster wie 语气词缺失, 翻译腔, 四字套语 |
| [Deutsch](rewild-de/SKILL.md) | 41 | Deutsch-spezifische Muster wie Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## So funktioniert's

1. Kopiere die `SKILL.md` für deine Sprache
2. Lass die passende `references/patterns.md` daneben liegen, damit das Modell Details bei Bedarf laden kann
3. Füge es als Skill in Claude Code / Cowork ein, oder als System Prompt in einem beliebigen LLM-Tool
4. Sag "rewild das" und füg deinen Text ein

## Aufbau

Jede Sprache ist in zwei Ebenen aufgeteilt:

- `SKILL.md`: Betriebsanleitung — Trigger-Regeln, Kernregeln, Seele-Anleitung, Genre-Kalibrierung, vollständiges Beispiel, Bewertungsraster
- `references/patterns.md`: Diagnosekatalog — sprachspezifische KI-Muster, Wörterlisten, Vorher/Nachher-Beispiele, akademische Quellen

Der Skill bleibt schnell ladbar. Der Musterkatalog wird bei Bedarf nachgeladen.

## Vorher / Nachher

**KI-generiert:**
> In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen. Darüber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung. Zusammenfassend lässt sich sagen, dass die Zukunft vielversprechend aussieht.

**Nach Rewild:**
> KI-Schreibwerkzeuge können das Schreiben erleichtern und Texte zugänglicher machen. Mehr muss man daraus aber nicht machen. "Nahtlos" und "innovativ" blähen den Absatz nur auf — die Zukunftsfloskel am Schluss erst recht.

## Deutsch-spezifische Muster

Rewild-DE erkennt 13 Muster, die nur im Deutschen auftreten:

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

## Eigenschaften der aktuellen Version

- Enger Trigger: nur bei explizitem KI-Ton-Problem
- Anti-Fabrikation: keine erfundenen Zahlen, Anekdoten oder Ich-Erlebnisse
- Genre-bewusst: formelle Texte bleiben formell
- Quellengebundene Seele: Stimme entsteht durch vorhandene Details, nicht durch Erfindung

---

## Autor

[Wallny](https://github.com/wallmage)
