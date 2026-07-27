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
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20%E7%B0%A1%20%7C%20%E6%B8%AF%20%7C%20%E5%8F%B0%20%7C%20DE-b45309?style=flat-square)](https://github.com/wallmage/rewild)
[![Blind A/B](https://img.shields.io/badge/blind%20A%2FB-83%25%20EN%20%C2%B7%2075%25%20ZH-2563eb?style=flat-square)](benchmarks/)
[![Region test](https://img.shields.io/badge/region%20attribution-50%2F50%20HK%20%C2%B7%20TW-16a34a?style=flat-square)](benchmarks/)
[![Editor review](https://img.shields.io/badge/native%20editor%20review-10%2F10%20HK%20%C2%B7%20TW-be123c?style=flat-square)](benchmarks/)

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體 · 香港](README.zh-HK.md) | [繁體 · 台灣](README.zh-TW.md) | [Deutsch](README.de.md)

KI-Text hat einen bestimmten Klang, und du kennst ihn. Aufgeblasene Bedeutsamkeit, Adjektiv-Drillinge, Zusammenfassungen, die eigentlich nichts sagen. Die meisten „Humanizer“-Tools schrubben genau diesen Klang weg und geben dir sauberen, seelenlosen Text zurück. Rewild macht etwas anderes: Es entfernt die KI-Muster und bringt deine Stimme zurück – Meinungen, Rhythmus, Ecken und Kanten. Es erfindet keine Fakten und verpasst dir keine Persönlichkeit, die vorher nicht da war.

**269 sprachspezifische Muster. Fünf Skills. Ein Checker, der deine Vorlage liest, nicht nur deinen Entwurf.**

## Funktioniert das wirklich

Gemessen wird dreierlei, und jede Messung beantwortet eine andere Frage.

**Ist diese Version besser als die vorherige?** Prüfer sehen beide Umschreibungen derselben Vorlage und müssen sich für eine entscheiden. Unentschieden ist nicht erlaubt, deshalb kann der Test nicht sättigen wie eine Checkliste. Fünf Vorlagen, drei unabhängige Prüfer, niemand weiß, welches System welchen Text geschrieben hat.

| | Englisch | Chinesisch |
|---|---|---|
| Der Vorgängerversion vorgezogen | **10 / 12 (83 %)** | **9 / 12 (75 %)** |
| Liest sich weniger maschinell | ja | ja |

Für Chinesisch brauchte es drei Runden: 6/12, dann 7/12, dann 9/12. Jede Runde hat einen echten Fehler behoben. Ein Beispiel: An vier Stellen behandelte der chinesische Skill satzfinale Modalpartikeln als Soll, das erfüllt werden muss, und das Modell klebte prompt ein 啊 an eine interne E-Mail. Alle drei Prüfer haben genau diesen Satz abgelehnt. Partikeln sind jetzt eine Diagnose, kein Ziel.

**Liest sich der Hongkong-Text als Hongkong und der Taiwan-Text als Taiwan?** Genau das behaupten die traditionell-chinesischen Skills, also wird es direkt geprüft. Drei Vorlagen, drei Arme (`hk`, `tw` und eine allgemeine Kontrolle „schreib wie ein Mensch auf Traditionell-Chinesisch“), neun Ausgaben auf einzelne Buchstaben anonymisiert, drei Prüfer – einer neutral, einer als Hongkonger Leser, einer als taiwanischer Leser.

| | Ergebnis |
|---|---|
| Regionszuordnung der Skill-Ausgaben | **18 / 18** |
| Natürlichkeit in der eigenen Region | **6 / 6** |

Jeder Prüfer hat jeden Text auf der richtigen Seite verortet, 50/50 über vier Runden, und nichts wurde für Festlandschrift gehalten. Aussagekraft bekommt das Ergebnis erst dadurch, dass die Kontrolle nicht schlecht geschrieben war: Die Prüfer nannten sie flüssig und im Wortschatz überwiegend taiwanisch, weil ein ungeführtes Modell von sich aus zu 專案 und 使用者 greift. Nur festlegen konnte sie sich nicht. Allgemeines Traditionell-Chinesisch ist ein echtes Ergebnis, und es gehört zu niemandem.

**Wie gut kann ein einzelner Text werden?** Die Tests oben sind Vergleiche, und sobald beide Seiten stimmen, sagen sie nichts mehr. Deshalb gibt es eine dritte Messung ohne Deckel: ein Essay pro Region, bewertet von einem Prüfer, der durchgehend auf Traditionell-Chinesisch als Feuilleton-Chefredakteur mit dreißig Jahren Erfahrung promptet wird. Note von 1 bis 10, dazu jede Zeile zitiert, die maschinell klingt. Korrekturen einarbeiten, neu einreichen.

| | Hongkong | Taiwan |
|---|---|---|
| Erstfassung | 5 | 5 |
| Sieben Runden, jede mit neuem Prüfer | 5 → 8 | 5 → 8 |
| Strukturüberarbeitung, ein Redakteur durchgehend gehalten | 7 → 8 → 9 | 8 → 9 |
| Endurteil | **10 – 落版，唔使再改** | **10 – 簽字發稿** |

Der methodische Befund steckt in den beiden mittleren Zeilen: Rotierende Prüfer bleiben bei 8 stehen, jeder fängt bei null an und findet dieselbe Sorte Kleinkram. Erst ein Redakteur, der über alle Fassungen hinweg derselbe bleibt, ergibt einen monoton steigenden Verlauf. Und derselbe Vorbehalt wie beim Regionstest: Das sind Sprachmodelle, keine muttersprachlichen Leser. Protokoll und vollständiger Verlauf liegen in [`benchmarks/`](benchmarks/).

**Wortschatz sättigt, Struktur nicht.** Ab der zweiten Runde fand keiner der beiden Redakteure noch ein falsches Wort – 「字係香港人嘅字，骨係機器嘅骨」 / 「字是台灣人的字，結構是機器的結構」. Alles zwischen 8 und 10 war Verteilung, und die steht inzwischen als Muster in allen fünf Katalogen (siehe *Warum es funktioniert*).

**Ist es besser als ein generischer Humanizer?** Ein älterer Lauf ergab 30/30 gegen 24/30 bei einem typischen 24-Regeln-Tool, im Chinesischen 30/30 gegen 20/30. Behandle die Zahl als unbestätigt: Die Rohausgaben sind nicht erhalten, und der Lauf liegt vor den unten beschriebenen Checker-Korrekturen. Der Prüfstand liegt in [`benchmarks/`](benchmarks/), mit Vorlagen, Bewertungsraster, Kontroll-Prompt und Blindbewertungsverfahren, damit du es nachrechnen und mir widersprechen kannst.

> **Vorlage:** In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen. Darüber hinaus bietet unsere bahnbrechende Plattform eine nahtlose, intuitive und umfassende Nutzererfahrung.
>
> **Typisches Tool:** Wir haben eine Plattform gebaut, die Teams Zeit spart. Das Feedback ist bisher gut – erste Rückmeldungen deuten auf echte Zeitersparnis hin.
>
> **Rewild:** Die Plattform spart Zeit. Das ist eine faire Aussage. „Bahnbrechend“ ist der Teil, der aufgeblasen wirkt.

Das typische Tool schreibt Werbesprache in leisere Werbesprache um. Rewild benennt sie.

## Warum es funktioniert

Die meisten Humanizer arbeiten mit gut zwanzig generischen Regeln. „Darüber hinaus“ streichen, Satzlängen variieren, fertig. Das reicht für die Oberfläche und für sonst nichts. Die zusätzliche Arbeit steckt an sechs Stellen.

**Muster pro Sprache, nicht eine Liste für alle.** Englische KI überstrapaziert „testament“ und „landscape“ und stützt sich auf Geviertstriche. Chinesische KI lässt Modalpartikeln weg und stapelt Vier-Zeichen-Idiome. Deutsche KI vermeidet Modalpartikeln und zerlegt Komposita. Jede Sprache hat ihren eigenen Katalog, aufgebaut aus Forschungsergebnissen und echten Erkennungsdaten – und für Traditionell-Chinesisch nach *Region*, aus dem Grund weiter unten.

**Der Marker, der korrekten Wortschatz überlebt.** Sobald jedes einzelne Wort stimmt, verrät sich ein Ich-Text immer noch als maschinell, und zwar durch gleichmäßig verteiltes Handwerk: Jeder Absatz endet kurz und trocken, jedes eingeführte Detail wird später eingelöst, Konkretes ist rationiert – eine Zahl pro Absatz –, Füllwörter sind gestreut statt geballt, und das Schlussbild deckt sich eins zu eins mit dem Thema. Nichts davon ist schlecht geschrieben, und genau das ist der Beweis. Ein perfektes Ende gegen ein anderes zu tauschen hilft also nicht – 「換衫，唔係換人」. Es hilft nur, bereit zu sein, flach zu enden, ein Detail unaufgelöst liegen zu lassen und überall vage zu bleiben außer an einer einzigen Stelle. Das Muster steht in allen fünf Katalogen, im deutschen als Muster 32b, und die Prüfung dazu in jeder `SKILL.md`: die letzten Sätze aller Absätze untereinander schreiben und die Spalte ansehen.

**Alltagsregister, nicht nur Amtssprache.** Die Regionalkataloge waren stark bei Behörden-, Presse- und Geschäftssprache und hatten nichts darüber, wie jemand über sein eigenes Handy spricht – also über das, was man tatsächlich am häufigsten umschreibt. Jetzt steht es drin: 計數機/計算機/計算器 (Taschenrechner), 碌/滑/刷手機 (Scrollen), 讚好/按讚/點讚 (Liken), 尿袋/行動電源/充電寶 (Powerbank), dazu die Plattformnamen als Verben (WhatsApp 我 gegenüber 賴我), an denen sich ablesen lässt, wo jemand lebt. Zwei muttersprachliche Prüfer haben diese Tabellen gegengelesen und mehrere Zeilen gestrichen. Jeder Katalog führt jetzt seine eigene Sperrliste – Hongkong: 平板, 封鎖, 應用程式, 截圖, 充電器, 計算器; Taiwan: 結帳, 追蹤, 動態, 平板, 截圖, 限時動態, 計算機 –, lauter Wörter, die auf beiden Seiten ganz normal sind, und ein Regressionstest stellt sicher, dass keines davon je in einen Filter gerät. Ein bereits korrektes Wort zurückzuersetzen macht aus einem Regionsbefund einen Registerfehler, und der liest sich schlechter als das Problem, das er beheben sollte.

**Ein Schutz gegen Überkorrektur.** Wer jeden Text mit denselben drei Tricks bearbeitet, Stakkato-Fragmenten und inszenierten Selbstkorrekturen und einer rhetorischen Frage pro Abschnitt, hat nur eine neue Schablone gebaut, die genauso maschinell klingt wie die alte. Rewild begrenzt seine Eingriffe und wechselt sie ab.

**Texttreue, nicht nur Stil.** Diesen Teil lassen die meisten Tools komplett aus. Eine Umschreibung kann nichts von der üblichen Liste erfinden, keine falschen Namen und keine falschen Zahlen, und trotzdem etwas behaupten, das die Vorlage nie gesagt hat. Vier Wege dorthin:

- Die Vorlage schreibt eine Behauptung jemandem zu; die Umschreibung streicht die Quelle und behält die Behauptung
- Die Vorlage beschreibt; die Umschreibung verspricht
- Die Vorlage sagt „beeinträchtigt“; die Umschreibung sagt „nichts ging mehr“
- Die Vorlage nennt eine Ursache; die Umschreibung schließt nebenbei andere aus

Die ersten drei findet der mitgelieferte Checker, indem er deine Umschreibung gegen deine Vorlage hält. Die vierte liegt beim Autor, und der Katalog sagt das auch so.

**Nichts erfinden, auch nichts Bescheidenes.** Jedes Detail im Ergebnis muss schon in der Vorlage stehen. Diese Regel hatte ein Loch: Eine ältere Version wies das Modell an, gestrichene Anpreisungen durch eine ehrliche, zurückhaltende Selbstaussage zu ersetzen – und es tat es. Ein Werbetext bekam einen Haftungsausschluss, den niemand geschrieben hatte. Eine Release-Notiz ließ eine Firma eine Schwäche einräumen, von der ihre eigene Vorlage nie sprach. Auch eine bescheidene Erfindung ist erfunden.

## Wie Rewild arbeitet

Für Hongkong und Taiwan läuft ein Durchgang vor allem anderen: ein Regionsscan über den ganzen Text nach Vokabular der anderen Region, ihren Umschriften, Festlandfloskeln und Zeichenfehlern. Er kommt zuerst, weil Regionsfehler nichts damit zu tun haben, ob ein Absatz sauber ist – ein Absatz ganz ohne KI-Marker kann trotzdem komplett von der falschen Seite der Taiwanstraße stammen.

Danach wird jeder Absatz sortiert, bevor irgendetwas angefasst wird. Dichten KI-Text Satz für Satz zu redigieren poliert nur das Skelett und lässt es stehen, deshalb teilt sich die Arbeit dreifach auf:

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
| [中文 vereinfacht](rewild-zh/SKILL.md) | 45 | Festlandchinesische Muster wie 语气词缺失, 翻译腔, 四字套语, 公式化开头 |
| [中文 traditionell · Hongkong](rewild-hk/SKILL.md) | 65 | Registerverzweigung 書面語/粵文, 「您」, 港式文言虛詞, 中英夾雜, 港式套語, 手機日常口語 |
| [中文 traditionell · Taiwan](rewild-tw/SKILL.md) | 65 | Japanisch geprägte Strukturen als heimisch geschützt, 台灣套語, 公文-Gerüst, 港式書信骨架, 社群日常口語 |
| [Deutsch](rewild-de/SKILL.md) | 48 | Deutsch-spezifische Muster wie Modalpartikeln, Komposita, Gedankenstrich, Konnektoren-Flut |

Hongkong und Taiwan sind zwei getrennte Skills, kein traditionell-chinesischer Skill mit Regionsschalter. Der Grund: **der heimische Wortschatz jeder Region überschneidet sich mit dem verbotenen Wortschatz der anderen.** 網絡, 智能 und 項目 sind Festlandwörter, die ein Taiwan-Skill entfernen muss – und zugleich Hongkonger Wörter, die ein Hongkong-Skill schützen muss. Eine einzige Sperrliste kann beide Regeln nicht enthalten, und ein nicht gesetzter Regionsschalter lässt das Modell mitteln: grammatisch korrektes Traditionell-Chinesisch, das zu niemandem gehört.

Keiner der beiden Kataloge ist eine Übersetzung des festlandchinesischen. Alle 45 Muster wurden einzeln geprüft: Hongkong behält 29, passt 15 an, streicht 1; Taiwan behält 25, passt 19 an, streicht 1. Dazu kommen je 21 Regionsmuster. Einige Anpassungen sind Widerrufe – Regeln, die normales lokales Schreiben als KI-Text markiert hätten.

## So funktioniert's

1. Kopiere den Skill-Ordner deiner Sprache (`rewild/`, `rewild-zh/`, `rewild-hk/`, `rewild-tw/` oder `rewild-de/`) in dein Skill-Verzeichnis, bei Claude Code ist das `~/.claude/skills/`. Ordnernamen und Inhalt so lassen: Der Ordnername entspricht dem `name:`-Feld des Skills, und der `references/`-Katalog und der `scripts/`-Checker gehören dazu.
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

Für `--lang hk` und `--lang tw` kommt eine dritte Hälfte dazu, die den Stilprüfungen vollständig entgeht: Vokabular der jeweils anderen Region, festlandtypisches Vokabular, die Umschriften der anderen Seite, nach der Konvertierung übrig gebliebene Kurzzeichen, die regionalen Zeichenstandards (裏/裡, 着/著) – und die **Floskeln**, die eine Regionalkonvertierung fast immer stehen lässt.

Ein weiterer Modus prüft, was jede Einzeldokumentprüfung strukturell nicht sehen kann: Schreibt man fünf verwandte Texte in einem Zug um, konvergieren sie – gleiche Absatzzahl, gleicher Schluss – während jeder einzeln sauber durchläuft:

```bash
python3 rewild-de/scripts/naturalness-check.py --siblings a.txt b.txt c.txt --lang de
```

Jeder Fehler, mit dem der Checker je ausgeliefert wurde, ist durch einen Regressionstest abgedeckt – inzwischen 146 statt anfangs 30:

```bash
python3 tests/test_checker.py
```

## Aufbau

Jede Sprache besteht aus zwei Dateien plus einem Skript, und die Trennung hat einen Grund.

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
- 教育部《兩岸常用詞典》 – Wortschatz beiderseits der Taiwanstraße, samt 港澳-Spalte
- 香港《政府公文寫作手冊》 (3. Aufl.) und 邵敬敏〈香港詞語的特點〉 – Hongkonger Register und der AB/BA-Umkehrsatz
- 台灣《法律統一用字表》 und 《常用字字形表》 – die Standards zu 布/佈 und 裡/裏
- 2.934 Pressemitteilungen der Hongkonger Regierung (info.gov.hk, Mai bis Juli 2026, 8,2 Mio. Zeichen) – Häufigkeitsbelege für die 港式套語-Liste

## Hinweise zur Auslieferung

- Greift nur, wenn du das Problem ausdrücklich als KI-Sound beschreibst
- Fügt keine Kennzahl, Anekdote oder Erfahrung hinzu, die deine Vorlage nicht hatte
- Formelle Texte bleiben formell
- Stimme entsteht aus Details, die schon im Text stehen
- Jede Umschreibung wird vor der Abgabe blind geprüft und gegen die Vorlage abgeglichen
- Für Hongkong und Taiwan gilt Vokabular der falschen Region als Fehler, nicht als Stilfrage

---

## Autor

[Wallny](https://github.com/wallmage)
