---
name: rewild-de
description: Nur verwenden, wenn der Nutzer ausdrücklich sagt, dass ein Text nach KI klingt, zu roboterhaft ist oder "humanisiert" bzw. "de-AI't" werden soll. Geeignet für Anfragen wie "klingt wie ChatGPT", "mach das menschlicher", "nimm den KI-Ton raus" oder "rewild das". Nicht für normales Lektorat, Korrektorat, Übersetzung, Zusammenfassung oder allgemeine Stilpflege auslösen, solange der Nutzer das Problem nicht ausdrücklich als KI-Sound beschreibt.
---

# Rewild-DE

Entfernt KI-Schreibmuster, ohne den Text in erfundene Details, unnötige Lockerheit oder eine andere Stimme kippen zu lassen.

## Wann verwenden / wann nicht

Verwenden:
- wenn der Nutzer explizit von KI-Ton, Robotersprache oder ChatGPT-Sound spricht
- wenn "humanisieren", "de-AI'n" oder "rewild" ausdrücklich gewünscht ist

Nicht verwenden:
- für normales Korrekturlesen
- für Grammatik- oder Rechtschreibkorrekturen
- für Übersetzungen
- für Zusammenfassungen
- für allgemeines "mach's besser", solange KI nicht das eigentliche Problem ist

## Kernregeln

- Stil ändern, Fakten behalten.
- Niemals Namen, Orte, Daten, Zahlen, Zitate, Anekdoten oder Ich-Erlebnisse erfinden.
- Zitate, Links, Code, Fachbegriffe, juristische Formulierungen und präzise Zahlen erhalten, sofern der Nutzer nicht ausdrücklich deren Umschreibung will.
- Zum Genre passen. Menschlich heißt nicht automatisch lockerer.
- Klingt die Vorlage schon natürlich, nur minimal eingreifen.
- Ist die Vorlage vage, ehrlicher und klarer schreiben statt falsche Konkretheit hinzuzufügen.

## Schnell-Checkliste

Vor der Abgabe jeden Text prüfen:

- Drei aufeinanderfolgende Sätze gleich lang? Einen aufbrechen
- Absatz endet mit einem ordentlichen Einzeiler? Abschluss variieren
- Geviertstrich (—) statt Halbgeviertstrich (–)? Sofort korrigieren
- Metapher wird erklärt? Dem Leser vertrauen
- "Darüber hinaus" / "Zusammenfassend lässt sich sagen"? Streichen
- Dreiergruppe? Zwei oder vier daraus machen
- Kein "Ich" im ganzen Text? Einfügen wo die Vorlage es trägt
- Keine Eigennamen? Aus der Vorlage vorhandene Namen nach vorn holen
- Keine Modalpartikeln (doch, halt, mal, eben, ja)? In informellen Texten mindestens eine einfügen
- Kein zusammengesetztes Substantiv? Komposita nutzen
- Nur Passiv-Sätze? Aktivsätze einmischen
- Jeder Absatz mit Konnektor? Hälfte streichen

## Persönlichkeit und Seele

KI-Muster zu vermeiden ist nur die halbe Arbeit. Steriler, stimmloser Text ist genauso offensichtlich wie Slop. Gutes Schreiben hat einen Menschen dahinter.

Zeichen seelenlosen Schreibens (auch wenn technisch "sauber"):
- Jeder Satz gleich lang und gleich gebaut
- Keine Meinungen, nur neutrales Berichten
- Keine Unsicherheit oder gemischte Gefühle
- Kein Ich, kein Du — nur man und es
- Keine Modalpartikeln — klingt wie ein Lehrbuch
- Liest sich wie ein Wikipedia-Artikel oder eine Pressemitteilung

Wie man Stimme reinbringt, ohne zu erfinden:

Hab eine Meinung. "Ich weiß ehrlich gesagt nicht, was ich davon halten soll" ist menschlicher als neutral Pro und Contra aufzulisten.

Variier den Rhythmus. Kurze Sätze. Dann ein längerer, der sich Zeit nimmt. Mischen.

Gib Unsicherheit zu. "Beeindruckend, aber auch irgendwie beunruhigend" schlägt "beeindruckend."

Benutz "Ich" wenn die Vorlage es trägt. Erste Person ist nicht unprofessionell — sie ist ehrlich.

Nutz Modalpartikeln. "Das ist doch klar" statt "Das ist klar." Doch, halt, mal, eben, ja, schon, wohl, eigentlich — das sind die Gewürze der deutschen Sprache. Nur in informellen Texten einsetzen, nicht erzwingen.

Nenn Dinge beim Namen. Vorhandene Namen, Orte und Details aus der Vorlage nach vorn holen. Nicht "ein führendes Tech-Unternehmen" sondern den Namen, der im Text steht.

Lass Unordnung zu. Abschweifungen und halbfertige Gedanken sind menschlich.

ENTSCHEIDENDE EINSCHRÄNKUNG: Jedes Detail, das du hinzufügst, muss bereits im Ausgangstext stehen oder daraus klar ableitbar sein. Keine erfundenen Treffen, Anekdoten, Statistiken, Firmennamen, Städtenamen oder Ich-Erlebnisse.

## Ablauf

1. Erst prüfen, ob das Problem wirklich KI-Ton ist und nicht eher Struktur, Grammatik oder Sachlichkeit.
2. Nicht umschreibbare Zonen markieren: Zitate, Links, Code, Fachsprache, präzise Zahlen, Compliance- und Rechtsformeln.
3. Genre und Risikoniveau bestimmen.
4. Mindestens D1-D7 in [references/patterns.md](references/patterns.md) prüfen. Die übrigen Muster bei konkreten Symptomen nachschlagen.
5. Nur die wirklich auffälligen Stellen umschreiben.
6. Schnell-Checkliste durchlaufen.
7. Zum Schluss Rhythmus, Natürlichkeit und Faktentreue prüfen.

## Genre-Kalibrierung

Informelle Texte, Blogposts, Essays:
- Mehr Rhythmus und eine klarere Stimme sind oft passend.
- "Ich", Nebenbemerkungen oder Lockerheit nur verwenden, wenn die Ausgangsstimme das trägt.

Geschäftstexte:
- Hype, Selbstbeweihräucherung und leere Bedeutungssätze entfernen.
- Professionellen Ton beibehalten.

Technische Dokumentation:
- Klarheit und Präzision vor Persönlichkeit.
- Keine künstliche Lockerheit einbauen.

Akademische, behördliche und formelle Texte:
- Vage Zuschreibungen, Werbesprache und Formelfloskeln abbauen.
- Formell bleiben; keine Modalpartikeln oder "du" erzwingen.

Recht, Medizin, Support, Richtlinien:
- Konservativ umschreiben.
- Genauigkeit und Konsistenz gehen vor.

## Ausgabe

Liefere:
1. den umgeschriebenen Text
2. optional eine kurze Notiz zu den wichtigsten entfernten KI-Mustern

Nur bewerten, wenn der Nutzer ausdrücklich eine Bewertung verlangt.

## Qualitätsbewertung (nur auf Anfrage)

| Dimension | Bewertungskriterium | Punkte |
|-----------|---------------------|--------|
| Direktheit | Sagt direkt was Sache ist oder erzählt drumherum? 10: auf den Punkt; 1: überall Einleitungen | /10 |
| Rhythmus | Satzlängen variiert? 10: kurz/lang gemischt; 1: metronomisch gleichförmig | /10 |
| Vertrauen | Respektiert den Leser? 10: knapp; 1: übererklärt alles | /10 |
| Authentizität | Klingt wie ein echter Mensch? 10: natürlich, mit Meinung und Modalpartikeln; 1: Lehrbuch | /10 |
| Präzision | Benutzt genaue Wörter, Namen, Zahlen? 10: kein Füllmaterial; 1: vage Abstraktionen | /10 |
| Gesamt | | /50 |

45-50: Ausgezeichnet. 35-44: Gut, noch Raum. Unter 35: Braucht eine weitere Runde.

## Vollständiges Beispiel

Vorher (KI-Deutsch):
> In der heutigen Zeit ist es wichtiger denn je, sich mit dem Thema künstliche Intelligenz auseinanderzusetzen. Darüber hinaus bieten KI-Schreibwerkzeuge eine nahtlose, intuitive und umfassende Nutzererfahrung — effizient, präzise und innovativ. Zusammenfassend lässt sich sagen, dass die Zukunft vielversprechend aussieht und spannende Entwicklungen bevorstehen.

Nachher (humanisiert):
> KI-Schreibwerkzeuge können das Schreiben erleichtern und Texte zugänglicher machen. Mehr muss man daraus aber nicht machen. Die Zukunftsfloskel am Schluss und Wörter wie "nahtlos" oder "innovativ" blähen den Absatz nur auf.

Änderungen:
- "In der heutigen Zeit" gestrichen (formelhafte Eröffnung, D7)
- "Darüber hinaus" gestrichen (KI-Konnektor, D6)
- "nahtlose, intuitive und umfassende" gestrichen (Dreier-Adjektiv, Muster 23)
- Geviertstrich korrigiert (D2)
- "Zusammenfassend lässt sich sagen" gestrichen (D6)
- "effizient, präzise und innovativ" gestrichen (Dreier-Adjektiv, Muster 23)
- Zukunftsfloskel benannt statt nur gelöscht

## Referenzdateien

- [references/patterns.md](references/patterns.md): detaillierter Musterkatalog und Umschreibhilfen

## Quellenhinweis

Basiert auf Wikipedia "Signs of AI writing", KONVENS 2024 (Irrgang et al.), De Gruyter 2025, ADVERTEXT, Kathrin Landsdorfer, ContentConsultants, WORTLIGA, fyrfeed, und den internationalen Quellen aus Tercon & Dobrovoljc (2025) u.a.
