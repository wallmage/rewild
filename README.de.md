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

KI-Text hat einen bestimmten Klang. Du kennst ihn: aufgeblasene Bedeutsamkeit, Adjektiv-Drillinge, Zusammenfassungen, die eigentlich nichts sagen. Die meisten „Humanizer“-Tools schrubben diesen Klang halt weg und lassen sauberen, aber seelenlosen Text stehen. Rewild macht was anderes. Es entfernt die KI-Muster und bringt *deine* Stimme zurück – Meinungen, Rhythmus, Ecken und Kanten. Keine erfundenen Fakten, keine aufgesetzte Persönlichkeit. Einfach der Text, den du eigentlich schreiben wolltest.

**30/30 im Benchmark. 40+ sprachspezifische Muster. Drei Sprachen.**

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

Die ersten drei Zeilen sind praktisch Gleichstand – KI-Vokabular entfernen kann doch jedes halbwegs brauchbare Tool. Der Unterschied liegt in den letzten beiden Zeilen: echte Details einbauen und eine Haltung zeigen. Ein typisches Tool hört beim Entfernen auf. Sauberer Text, keine Seele. Rewild erreicht 30/30, weil „klingt nicht nach KI“ erst der Anfang ist, nicht das Ziel. Es stellt den Rhythmus wieder her, schiebt echte Details aus dem Quelltext nach vorne und lässt den Text eben mal eine Meinung haben.

**Chinesisch-Benchmark:** Der Abstand ist da noch größer – **30/30 (100%)** vs. **20/30 (67%)**. Generische Tools haben null chinesisch-spezifische Muster und erkennen daher keine fehlenden Modalpartikeln (语气词), keine Idiom-Häufungen (四字套语) oder Übersetzungs-Stil (翻译腔).

Der Prüfstand liegt in [`benchmarks/`](benchmarks/) – Eingaben, Bewertungsraster, Kontroll-Prompt und Blindbewertungsverfahren –, damit man das nachrechnen kann, statt der Zahl zu glauben. Die Rohausgaben des ursprünglichen Laufs sind nicht erhalten; wenn dein Durchlauf etwas anderes ergibt, gehört die Zahl oben geändert.

## Warum Rewild funktioniert

Die meisten Humanizer arbeiten mit knapp zwanzig generischen Regeln: „Additionally“ löschen, Satzlänge variieren, fertig. Damit kriegt man die Oberfläche hin. Rewild geht in vier Punkten tiefer:

**40+ sprachspezifische Muster statt 20 generischer Regeln.** Jede Sprache hat halt ihre eigenen KI-Marker. Englische KI überstrapaziert „testament“, „landscape“ und Geviertstriche. Deutsche KI vermeidet Modalpartikeln, zerlegt Komposita und schreibt „In der heutigen Zeit“ als Einstieg. Rewild hat für jede Sprache einen eigenen Musterkatalog, der auf Forschungsergebnissen und echten Erkennungsdaten basiert.

**Zwei-Schichten-Architektur.** Eine schlanke `SKILL.md` (die Betriebsanleitung) lädt schnell und legt die Regeln fest. Ein ausführlicher `references/patterns.md` (der Diagnosekatalog) wird bei Bedarf nachgeladen – Wortlisten, Vorher/Nachher-Beispiele, akademische Quellen. So bekommt man Präzision, ohne das gesamte Kontextfenster beim Start zu verbrauchen.

**Anti-Fabrikation als Kernregel.** Viele Tools „humanisieren“, indem sie Anekdoten erfinden, Fake-Statistiken einstreuen oder Ich-Erlebnisse dazudichten. Das macht Rewild nicht. Jedes Detail im Output muss schon im Quelltext stehen. Stimme entsteht durch Rhythmus, Haltung und das Hervorbringen echter Details – nicht durch Erfinden.

**Ein Schutz gegen Überkorrektur.** Wer jeden Text mit denselben drei Tricks humanisiert – Stakkato-Fragmente, inszenierte Selbstkorrekturen, rhetorische Fragen – baut nur eine neue, genauso erkennbare Schablone. Rewild begrenzt die Eingriffe pro Text und wechselt die Mittel, damit zehn Umschreibungen nicht in derselben Stimme enden.

## So arbeitet Rewild

Rewild sortiert jeden Absatz, bevor es ihn anfasst. Dichten KI-Text Satz für Satz zu redigieren poliert nur das Skelett und lässt es stehen, deshalb teilt der Ablauf die Arbeit dreifach auf:

- **Schon menschlich?** Stehen lassen. Zu viel zu ändern ist die häufigste Art, wie solche Tools scheitern – ein sauberer Absatz bekommt nichts oder eine kleine Korrektur.
- **Ein paar Marker?** An Ort und Stelle gegen den Musterkatalog beheben.
- **Dichter Slop?** Neu sagen. Die Fakten notieren, vom Original wegschauen, den Absatz frisch im selben Register schreiben, dann jeden Fakt gegen die Vorlage abgleichen.

Formelle Genres sind die Ausnahme. Pressemitteilungen, Ankündigungen und Behördentexte werden gestrichen und gestrafft, nie komplett neu gesagt – ihr schriftliches Skelett ist das Register, und Neusagen rutscht in Plauderton. Komplettes Neusagen ist für Essays und Posts, wo die Stimme den Text trägt.

Vor der Auslieferung laufen zwei Prüfungen. Ein Prüfer mit leerem Kontext liest die Umschreibung blind und markiert, was noch nach KI klingt. Dann misst der mitgelieferte Checker die statistischen Marker, die das Modell im eigenen Text nicht sieht, und der Entwurf wird korrigiert, bis der Bericht sauber ist.

Wie viel bringt der Ablauf selbst? Weniger als man denkt. Zehn Vorlagen aus zehn Genres wurden von dieser und von der vorherigen Version umgeschrieben und dann von drei unabhängigen Prüfern blind bewertet. Das Ergebnis war gleichauf: 94,7 zu 93,3 von 100. Die Arbeit machen die Musterkataloge und der Checker; der Ablauftext hält das Ganze vor allem ehrlich. Der Test liegt in [`benchmarks/`](benchmarks/) und lässt sich nachfahren.

## Deutsch-spezifische Muster

Rewild-DE erkennt 13 Muster, die nur im Deutschen auftreten:

- **Modalpartikeln fehlen** – doch, halt, mal, eben, ja sind die Seele der deutschen Sprache; KI nutzt sie kaum. Ein Text ohne „halt“ oder „eben“ klingt sofort künstlich
- **Geviertstrich statt Halbgeviertstrich** – Englischer em dash (—) statt korrektem deutschen Halbgeviertstrich (–). Fällt vielleicht nicht jedem auf, ist aber ein klarer Marker
- **Falsche Anführungszeichen** – Englische "..." statt deutschen „...“ – das ist doch eigentlich ein Anfängerfehler
- **Hauptsatz-Ketten** – Kurze Hauptsätze aneinandergereiht, wo natürliches Deutsch Nebensätze bauen würde; im Nebensatz steht das Verb manchmal nicht am Ende
- **Komposita zerlegt** – „Taschen-Rechner“ statt Taschenrechner. KI hat da eben ein Problem mit der Zusammenschreibung
- **Konnektoren-Flut** – „Darüber hinaus“, „Zusammenfassend lässt sich sagen“ – das braucht man mal, aber nicht in jedem Absatz
- **Formelhafte Eröffnungen** – „In der heutigen Zeit...“ als Einstieg ist ein sofortiger KI-Marker
- **Kasusfehler** – „des Kunde“ statt „des Kunden“; schwache Maskulina sind eine klassische KI-Stolperfalle
- **Passiv-Ketten** – Drei Passivsätze hintereinander plus Nominalstil. Liest sich wie eine Behördenakte
- **Hedging-Konjunktiv** – „könnte möglicherweise potenziell“ als Dauerabsicherung, wo ein klares „dürfte“ oder „ist“ reicht
- **Wörtliche Übersetzungen** – „Sie nahm einen tiefen Atemzug“ statt „Sie atmete tief durch“
- **Fehlende regionale Färbung** – Kein Österreichisch, Schweizerdeutsch oder dialektale Einsprengsel
- **Orthographische Inkonsistenz** – Verschiedene Schreibweisen im selben Text

## Skills

| Skill | Muster | Besonderheit |
|-------|--------|--------------|
| [English](rewild/SKILL.md) | 42 | Schlankes `SKILL.md` + ausführlicher [pattern catalog](rewild/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 41 | Chinesisch-spezifische Muster wie 语气词缺失, 翻译腔, 四字套语 |
| [Deutsch](rewild-de/SKILL.md) | 44 | Deutsch-spezifische Muster wie Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## So funktioniert's

1. Kopiere den Skill-Ordner deiner Sprache (`rewild/`, `rewild-zh/` oder `rewild-de/`) in dein Skill-Verzeichnis – bei Claude Code ist das `~/.claude/skills/`. Ordnernamen und Inhalt so lassen: Der Ordnername entspricht dem `name:`-Feld des Skills, und der `references/`-Katalog und der `scripts/`-Checker gehören dazu.
2. Oder füge in einem anderen LLM die `SKILL.md` als System Prompt ein und halte `references/patterns.md` bereit, damit das Modell Details nachladen kann.
3. Sag „rewild das“ und füg deinen Text ein.

## Automatische Natürlichkeitsprüfung

Jeder Skill-Ordner bringt [`scripts/naturalness-check.py`](rewild-de/scripts/naturalness-check.py) mit (Python 3, keine Abhängigkeiten). Es misst die statistischen Marker aus den Katalogen: gleichförmige Satzlängen, wiederholte Satzanfänge, gleich lange Absätze, KI-Vokabular und Zeichensetzung – Geviertstriche, als Gedankenstrich missbrauchte Bindestriche und englische Anführungszeichen („Das stimmt.“ vs. “Das stimmt.”).

Der Lauf ist ein Pflichtschritt im Ablauf: Das Modell prüft jede Umschreibung und behebt Warnungen, bis der Bericht sauber ist – erst dann wird geliefert. Der Exit-Code ist 1, solange etwas markiert ist, und 0 bei sauberem Bericht, das Skript taugt also auch als Gate. Manuell geht es jederzeit auch:

```bash
python3 rewild-de/scripts/naturalness-check.py entwurf.txt --lang de
```

Markdown liest das Skript als Fließtext, nicht als Gerüst: Überschriften, Codeblöcke und Tabellenzeilen werden übersprungen, Listenpunkte zählen als eigene Sätze. Die Suche ist typografieunabhängig, und das Vokabular wird flektiert erkannt – „nahtlos“ findet auch „nahtlose“ und „nahtlosen“.

`--audit` vergleicht die Wortlisten des Skripts mit dem Musterkatalog daneben und meldet jeden Begriff, den der Katalog dokumentiert, das Skript aber nicht sieht. Nach jeder Katalogänderung einmal laufen lassen, dann driften die beiden nicht auseinander:

```bash
python3 rewild-de/scripts/naturalness-check.py --audit --lang de
```

Für den Checker selbst gibt es Regressionstests, die jeden Fehler abdecken, mit dem er ausgeliefert wurde. Aus dem Repo-Wurzelverzeichnis:

```bash
python3 tests/test_checker.py
```

## Aufbau

Jede Sprache besteht aus zwei Dateien, und diese Aufteilung ist Absicht.

`SKILL.md` ist die Betriebsanleitung. Sie definiert, wann das Tool anspringen soll, was nicht verändert werden darf, wie man für verschiedene Textsorten kalibriert und wie guter Stil klingt. Drin stecken eine Schnellreferenz-Checkliste, ein vollständiges Beispiel und ein Bewertungsraster. Das wird jedes Mal in den Kontext geladen.

`references/patterns.md` ist der Diagnosekatalog. Hier liegt das komplette Inventar sprachspezifischer KI-Muster – Wortlisten, Vorher/Nachher-Beispiele für jedes Muster, Schweregrad-Einstufungen und akademische Quellen. Das Modell liest daraus bei Bedarf, und zwar nur die Abschnitte, die für den vorliegenden Text relevant sind.

Das Ergebnis: schneller Start, gründliche Diagnose bei Bedarf, kein verschwendeter Kontext. Die Betriebsanleitung kennt die Regeln. Der Katalog kennt die Muster. Zusammen funktionieren sie.

## Vorher / Nachher

**KI-generiert:**
> In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen. Darüber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung. Zusammenfassend lässt sich sagen, dass die Zukunft vielversprechend aussieht.

**Nach Rewild:**
> KI-Schreibwerkzeuge können das Schreiben erleichtern und Texte zugänglicher machen. Mehr muss man daraus aber nicht machen. „Nahtlos“ und „innovativ“ blähen den Absatz nur auf – die Zukunftsfloskel am Schluss erst recht.

## Quellen

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) – 44-Studien-Synthese
- KONVENS 2024 (Irrgang et al.) – Deutsche KI-Texterkennung
- De Gruyter 2025 – Linguistische Komplexitätsanalyse
- ADVERTEXT Lektoratstest
- Kathrin Landsdorfer – 21 ChatGPT-Phrasen
- ContentConsultants, WORTLIGA, fyrfeed

## Eigenschaften

- Enger Trigger: nur bei explizitem KI-Ton-Problem
- Anti-Fabrikation: keine erfundenen Zahlen, Anekdoten oder Ich-Erlebnisse
- Genre-bewusst: formelle Texte bleiben formell
- Quellengebundene Stimme: entsteht durch vorhandene Details, nicht durch Erfindung
- Zwei Durchgänge als Standard: Ein Subagent mit leerem Kontext prüft jede Umschreibung blind vor der Abgabe

---

## Autor

[Wallny](https://github.com/wallmage)
