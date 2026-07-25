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

KI-Text hat einen bestimmten Klang, und du kennst ihn. Aufgeblasene Bedeutsamkeit, Adjektiv-Drillinge, Zusammenfassungen, die eigentlich nichts sagen. Die meisten „Humanizer“-Tools schrubben genau diesen Klang weg und geben dir sauberen, seelenlosen Text zurück. Rewild macht etwas anderes: Es entfernt die KI-Muster und bringt deine Stimme zurück – Meinungen, Rhythmus, Ecken und Kanten. Es erfindet keine Fakten und verpasst dir keine Persönlichkeit, die vorher nicht da war.

**139 sprachspezifische Muster. Drei Sprachen. Ein Checker, der deine Vorlage liest, nicht nur deinen Entwurf.**

## Funktioniert das wirklich

Zwei Dinge werden gemessen, und sie beantworten verschiedene Fragen.

**Ist diese Version besser als die vorherige?** Prüfer sehen beide Umschreibungen derselben Vorlage und müssen sich für eine entscheiden. Unentschieden ist nicht erlaubt, deshalb kann der Test nicht sättigen wie eine Checkliste. Fünf Vorlagen, drei unabhängige Prüfer, niemand weiß, welches System welchen Text geschrieben hat.

| | Englisch | Chinesisch |
|---|---|---|
| Der Vorgängerversion vorgezogen | **10 / 12 (83 %)** | **9 / 12 (75 %)** |
| Liest sich weniger maschinell | ja | ja |

Für Chinesisch brauchte es drei Runden: 6/12, dann 7/12, dann 9/12. Jede Runde hat einen echten Fehler behoben. Ein Beispiel: An vier Stellen behandelte der chinesische Skill satzfinale Modalpartikeln als Soll, das erfüllt werden muss, und das Modell klebte prompt ein 啊 an eine interne E-Mail. Alle drei Prüfer haben genau diesen Satz abgelehnt. Partikeln sind jetzt eine Diagnose, kein Ziel.

**Ist es besser als ein generischer Humanizer?** Ein älterer Lauf ergab 30/30 gegen 24/30 bei einem typischen 24-Regeln-Tool, im Chinesischen 30/30 gegen 20/30. Behandle die Zahl als unbestätigt: Die Rohausgaben sind nicht erhalten, und der Lauf liegt vor den unten beschriebenen Checker-Korrekturen. Der Prüfstand liegt in [`benchmarks/`](benchmarks/), mit Vorlagen, Bewertungsraster, Kontroll-Prompt und Blindbewertungsverfahren, damit du es nachrechnen und mir widersprechen kannst.

> **Vorlage:** In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen. Darüber hinaus bietet unsere bahnbrechende Plattform eine nahtlose, intuitive und umfassende Nutzererfahrung.
>
> **Typisches Tool:** Wir haben eine Plattform gebaut, die Teams Zeit spart. Das Feedback ist bisher gut – erste Rückmeldungen deuten auf echte Zeitersparnis hin.
>
> **Rewild:** Die Plattform spart Zeit. Das ist eine faire Aussage. „Bahnbrechend“ ist der Teil, der aufgeblasen wirkt.

Das typische Tool schreibt Werbesprache in leisere Werbesprache um. Rewild benennt sie.

## Warum es funktioniert

Die meisten Humanizer arbeiten mit gut zwanzig generischen Regeln. „Darüber hinaus“ streichen, Satzlängen variieren, fertig. Das reicht für die Oberfläche und für sonst nichts. Die zusätzliche Arbeit steckt an vier Stellen.

**Muster pro Sprache, nicht eine Liste für alle.** Englische KI überstrapaziert „testament“ und „landscape“ und stützt sich auf Geviertstriche. Chinesische KI lässt Modalpartikeln weg und stapelt Vier-Zeichen-Idiome. Deutsche KI vermeidet Modalpartikeln und zerlegt Komposita. Jede Sprache hat ihren eigenen Katalog, aufgebaut aus Forschungsergebnissen und echten Erkennungsdaten.

**Ein Schutz gegen Überkorrektur.** Wer jeden Text mit denselben drei Tricks bearbeitet, Stakkato-Fragmenten und inszenierten Selbstkorrekturen und einer rhetorischen Frage pro Abschnitt, hat nur eine neue Schablone gebaut, die genauso maschinell klingt wie die alte. Rewild begrenzt seine Eingriffe und wechselt sie ab.

**Texttreue, nicht nur Stil.** Diesen Teil lassen die meisten Tools komplett aus. Eine Umschreibung kann nichts von der üblichen Liste erfinden, keine falschen Namen und keine falschen Zahlen, und trotzdem etwas behaupten, das die Vorlage nie gesagt hat. Vier Wege dorthin:

- Die Vorlage schreibt eine Behauptung jemandem zu; die Umschreibung streicht die Quelle und behält die Behauptung
- Die Vorlage beschreibt; die Umschreibung verspricht
- Die Vorlage sagt „beeinträchtigt“; die Umschreibung sagt „nichts ging mehr“
- Die Vorlage nennt eine Ursache; die Umschreibung schließt nebenbei andere aus

Die ersten drei findet der mitgelieferte Checker, indem er deine Umschreibung gegen deine Vorlage hält. Die vierte liegt beim Autor, und der Katalog sagt das auch so.

**Nichts erfinden, auch nichts Bescheidenes.** Jedes Detail im Ergebnis muss schon in der Vorlage stehen. Diese Regel hatte ein Loch: Eine ältere Version wies das Modell an, gestrichene Anpreisungen durch eine ehrliche, zurückhaltende Selbstaussage zu ersetzen – und es tat es. Ein Werbetext bekam einen Haftungsausschluss, den niemand geschrieben hatte. Eine Release-Notiz ließ eine Firma eine Schwäche einräumen, von der ihre eigene Vorlage nie sprach. Auch eine bescheidene Erfindung ist erfunden.

## Wie Rewild arbeitet

Jeder Absatz wird sortiert, bevor irgendetwas angefasst wird. Dichten KI-Text Satz für Satz zu redigieren poliert nur das Skelett und lässt es stehen, deshalb teilt sich die Arbeit dreifach auf:

- **Schon menschlich?** Stehen lassen. Zu viel zu ändern ist die häufigste Art, wie solche Tools scheitern, also bekommt ein sauberer Absatz nichts oder eine Kleinigkeit.
- **Ein paar Marker?** An Ort und Stelle gegen den Katalog beheben.
- **Dichter Slop?** Neu sagen. Die Fakten notieren, vom Original wegschauen, im selben Register frisch schreiben, dann jeden Fakt gegen die Vorlage abgleichen.

Neusagen ändert die Formulierung, nie die Reihenfolge. Wer die als „wichtigste“ angekündigte Lehre eines Essays ans Ende schiebt, lässt den Aufbau davor ins Leere laufen.

Formelle Genres sind vom Neusagen ganz ausgenommen. Pressemitteilungen, Ankündigungen und Behördentexte werden stattdessen gestrichen und gestrafft, weil ihr schriftliches Gerüst selbst das Register ist und Neusagen in Plauderton rutscht.

Vor der Auslieferung laufen zwei Prüfungen. Ein Prüfer ohne Erinnerung an das Original liest die Umschreibung blind und markiert, was noch nach KI klingt. Dann misst der Checker, was das Modell im eigenen Text nicht sieht, und hält den Entwurf gegen die Vorlage. Stil-Warnungen sind Vorschläge. Treue-Warnungen sind Fehler.

## Skills

| Skill | Muster | Besonderheit |
|-------|--------|--------------|
| [English](rewild/SKILL.md) | 46 | Schlankes `SKILL.md` + ausführlicher [pattern catalog](rewild/references/patterns.md) |
| [中文](rewild-zh/SKILL.md) | 45 | Chinesisch-spezifische Muster wie 语气词缺失, 翻译腔, 四字套语 |
| [Deutsch](rewild-de/SKILL.md) | 48 | Deutsch-spezifische Muster wie Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

## So funktioniert's

1. Kopiere den Skill-Ordner deiner Sprache (`rewild/`, `rewild-zh/` oder `rewild-de/`) in dein Skill-Verzeichnis, bei Claude Code ist das `~/.claude/skills/`. Ordnernamen und Inhalt so lassen: Der Ordnername entspricht dem `name:`-Feld des Skills, und der `references/`-Katalog und der `scripts/`-Checker gehören dazu.
2. In einem anderen LLM fügst du `SKILL.md` als System Prompt ein und hältst `references/patterns.md` bereit, damit das Modell nachladen kann.
3. Sag „rewild das“ und füg deinen Text ein.

## Der mitgelieferte Checker

Jeder Skill-Ordner bringt [`scripts/naturalness-check.py`](rewild-de/scripts/naturalness-check.py) mit, Python 3 ohne Abhängigkeiten. Der Lauf ist Pflichtschritt im Ablauf, kein Extra.

Gib die Vorlage zusammen mit der Umschreibung mit, dann erledigt er beide Hälften:

```bash
python3 rewild-de/scripts/naturalness-check.py umschreibung.txt --source vorlage.txt --lang de
```

Die Stil-Hälfte misst, was die Kataloge beschreiben: gleichförmige Satzlängen, wiederholte Satzanfänge, gleich lange Absätze, KI-Vokabular, Zeichensetzung. Die Treue-Hälfte vergleicht beide Texte und meldet Namen, Zahlen, Zusagen, übernommene Zuschreibungen und aufgeblasenen Schweregrad. Der Exit-Code ist 1, solange etwas markiert ist, und 0 bei sauberem Bericht, damit das Skript auch als Gate taugt.

Ein paar Dinge macht er richtig, die eine naive Umsetzung falsch macht. Markdown liest er als Fließtext statt als Gerüst: Überschriften, Codeblöcke und Tabellenzeilen werden übersprungen, Listenpunkte zählen als eigene Sätze. Die Suche ist typografieunabhängig. Vokabular wird flektiert erkannt, „nahtlos“ findet auch „nahtlose“ und „nahtlosen“. Für Deutsch prüft er zusätzlich Geviertstriche, als Gedankenstrich missbrauchte Bindestriche und englische Anführungszeichen.

Nach jeder Katalogänderung einmal `--audit` laufen lassen. Es vergleicht die Wortlisten des Skripts mit dem Katalog daneben und meldet jeden Begriff, den der Katalog dokumentiert, das Skript aber nicht sieht:

```bash
python3 rewild-de/scripts/naturalness-check.py --audit --lang de
```

Dreißig Regressionstests decken jeden Fehler ab, mit dem der Checker je ausgeliefert wurde:

```bash
python3 tests/test_checker.py
```

## Aufbau

Jede Sprache besteht aus zwei Dateien, und die Trennung hat einen Grund.

`SKILL.md` ist die Betriebsanleitung: wann der Skill greift, was unangetastet bleibt, wie nach Genre kalibriert wird, wie Stimme klingt. Sie lädt jedes Mal in den Kontext, also bleibt sie schlank.

`references/patterns.md` ist der Diagnosekatalog: das vollständige Inventar der Marker, mit Wortlisten, Vorher/Nachher-Paaren und Quellen. Das Modell holt sich Abschnitte bei Bedarf, statt alles vorab zu laden.

Ein Ergebnis aus den Tests hat mich überrascht: Wo eine Regel steht, zählt so viel wie ihre Formulierung. Die Treue-Regeln standen zuerst am Ende des Abschnitts über Stimme, also war das Letzte, was das Modell vor dem Schreiben las, eine Liste von Verboten. Es schrieb zaghaft und verlor den Blindvergleich mit 5/12. Derselbe Text, nur in einen Prüfabschnitt nach dem Entwurf verschoben: 10/12.

## Vorher / Nachher

**KI-Deutsch:**
> In der heutigen Zeit ist es wichtiger denn je, sich mit dem Thema künstliche Intelligenz auseinanderzusetzen. Darüber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung. Zusammenfassend lässt sich sagen, dass die Zukunft vielversprechend aussieht.

**Rewild:**
> KI-Schreibwerkzeuge können das Schreiben erleichtern und Texte zugänglicher machen. Mehr muss man daraus aber nicht machen. Die Zukunftsfloskel am Schluss bläht den Absatz nur auf.

## Quellen

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) – 44-Studien-Synthese
- KONVENS 2024 – Erkennung deutscher KI-Texte
- De Gruyter 2025 – Analyse sprachlicher Komplexität im Deutschen
- Huxiu – quantitative Analyse chinesischer Stilmittel
- AIGCleaner – chinesische Erkennungsgewichte

## Hinweise zur Auslieferung

- Greift nur, wenn du das Problem ausdrücklich als KI-Sound beschreibst
- Fügt keine Kennzahl, Anekdote oder Erfahrung hinzu, die deine Vorlage nicht hatte
- Formelle Texte bleiben formell
- Stimme entsteht aus Details, die schon im Text stehen
- Jede Umschreibung wird vor der Abgabe blind geprüft und gegen die Vorlage abgeglichen

---

## Autor

[Wallny](https://github.com/wallmage)
