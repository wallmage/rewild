# Rewild-DE Musterkatalog

Erst `SKILL.md` lesen. Diese Datei ist die Nachschlagehilfe für Diagnosen und Umschreibungen.

Hinweis: Die Vorher/Nachher-Paare unten sind Lehrbeispiele, die jedes Muster illustrieren. Das "Nachher" zeigt gutes menschliches Deutsch für dieses Muster, nicht eine wortwörtliche Umschreibung des "Vorher"-Textes. Beim echten Umschreiben nur Details verwenden, die bereits im Ausgangstext stehen.

Außerdem: Jedes "Nachher" zeigt ein Muster isoliert. Nicht alle Mittel in eine einzige Umschreibung stapeln – das erzeugt eine eigene Schablone (siehe Muster 42).

## Höchste Priorität: deutschspezifische Muster

D1. Fehlende Modalpartikeln (stärkstes deutsches KI-Merkmal).
Problem: Modalpartikeln wie doch, halt, mal, eben, ja, schon, wohl, eigentlich, übrigens sind fundamental für natürliches Deutsch. Sie vermitteln Sprecherhaltung, mildern Aussagen, drücken Überraschung aus. KI benutzt sie fast nie, weil sie kein semantisches Eigengewicht haben und nicht ins Englische übersetzbar sind.

Vorher:
> Das ist richtig. Dieser Ansatz funktioniert. Wir sollten weitermachen.

Nachher:
> Stimmt schon – der Ansatz funktioniert ja. Dann sollten wir da auch dranbleiben.

Fix: in informellem Text natürlich einsetzen. Nicht in jeden Satz, aber da wo der Tonfall es braucht. Zwei, drei Partikeln pro Absatz reichen – ein Text, in dem jeder Satz halt, doch oder eben enthält, ist genauso auffällig wie einer ganz ohne. In formellen Texten nicht erzwingen.

D2. Geviertstrich statt Halbgeviertstrich.
Problem: Englisch nutzt den Geviertstrich (—), Deutsch den Halbgeviertstrich (–) mit Leerzeichen beidseitig. KI setzt Geviertstriche in deutschen Text.

Vorher:
> Die Ergebnisse—sauber, effizient und ganzheitlich—sprechen für sich.

Nachher:
> Die Ergebnisse – sauber und effizient – sprechen für sich.

Fix: jeden — durch – mit Leerzeichen ersetzen.

D3. Falsche Anführungszeichen.
Problem: Deutsche Anführungszeichen öffnen unten („) und schließen oben (“). Verlage nutzen auch »…«, die Schweiz «…». KI setzt englische ("…" oder “…”) oder wechselt mitten im Text die Konvention.

Vorher:
> Er sagte: "Das stimmt."

Nachher:
> Er sagte: „Das stimmt.“

Fix: englische Anführungszeichen durch „…“ ersetzen (bzw. »…« oder «…», wenn der Text diese Konvention nutzt). Eine Konvention wählen und durchhalten.

D4. Hauptsatz-Ketten statt Nebensätzen.
Problem: Natürliches Deutsch lebt von Hypotaxe – Nebensätze mit Verb am Ende, Einschübe, Relativsätze. KI-Deutsch reiht stattdessen kurze Hauptsätze aneinander, weil es syntaktisch einfache Strukturen bevorzugt (De Gruyter 2025). Gelegentlich steht in Nebensätzen das Verb zu früh.

Vorher:
> Wir haben das Projekt verschoben. Der Kunde hatte neue Anforderungen. Das Budget war noch nicht freigegeben.

Nachher:
> Wir haben das Projekt verschoben, weil der Kunde neue Anforderungen hatte und das Budget noch nicht freigegeben war.

Fix: Hauptsatz-Ketten gelegentlich unterordnen. Nebensatz-Wortstellung prüfen (konjugiertes Verb ans Ende).

D5. Zerlegte Komposita.
Problem: Deutsch ist berühmt für beliebig lange Zusammensetzungen. KI zerlegt sie mit unnötigem Bindestrich oder umschreibt sie analytisch.

Vorher:
> Der Taschen-Rechner und der Online Shop bieten viele Funktionen.

Nachher:
> Der Taschenrechner und der Onlineshop bieten viele Funktionen.

Fix: zusammenschreiben. Bindestriche nur bei Anglizismen (AI-Modell) oder zur Lesbarkeit bei drei+ Gliedern.

D6. Übermäßige Konnektoren.
Hochfrequente KI-Konnektoren: Darüber hinaus, Zudem, Folglich, Zusätzlich, Nichtsdestotrotz, Zusammenfassend lässt sich sagen, Abschließend lässt sich sagen, Infolgedessen

Vorher:
> Darüber hinaus ist es wichtig zu beachten, dass die Lösung effizient ist. Zudem bietet sie eine intuitive Benutzeroberfläche. Folglich steigt die Nutzerzufriedenheit. Zusammenfassend lässt sich sagen, dass das Produkt überzeugt.

Nachher:
> Die Lösung ist effizient und die Oberfläche einfach zu bedienen. Die Nutzer sind zufrieden – das reicht doch als Beweis.

Fix: mindestens die Hälfte streichen.

D7. Formelhafte Eröffnungen und Schlüsse.
Todesphrasen (Anfang): In der heutigen Zeit ist es wichtiger denn je..., In einer Welt, in der..., Im digitalen Zeitalter..., Immer mehr Menschen fragen sich..., Seit jeher...
Todesphrasen (Schluss): Zusammenfassend lässt sich sagen, Abschließend bleibt festzuhalten, Insgesamt zeigt sich, Fazit: ..., Es bleibt spannend, Die Zukunft wird zeigen, ob...

Vorher:
> In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen.

Nachher:
> Letzten Monat hat mein Chef ChatGPT unsere Quartalszahlen zusammenfassen lassen. Das Ergebnis las sich wie eine Laudatio auf eine Firma, die es gar nicht gibt.

Fix: mit einer Anekdote, Szene, Frage oder konkretem Beispiel anfangen. Nie mit "In der heutigen Zeit." Am Schluss auf der stärksten konkreten Aussage enden, nicht auf einer Bilanzfloskel.

D8. Kasusfehler und Register-Genitiv.
Problem: KI dekliniert schwache Maskulina falsch (des Kunde statt des Kunden). Und in betont mündlichen Texten wirkt ihr strikter Genitiv nach wegen/trotz steifer, als ein Mensch dort schreiben würde.

Vorher:
> Die Beschwerde des Kunde wurde an das zuständige Team weitergeleitet.

Nachher:
> Die Beschwerde des Kunden wurde an das zuständige Team weitergeleitet.

Fix: schwache Maskulina korrekt deklinieren (des Kunden, dem Experten, den Kollegen). Im geschriebenen Standard bleibt der Genitiv nach wegen/trotz korrekt – Dativ ("wegen dem Wetter") nur, wenn der Text bewusst gesprochene Sprache abbildet.

D9. Passiv-Ketten und Nominalstil.
Problem: KI übernutzt Passiv-Konstruktionen und Nominalisierungen. Drei Passiv-Sätze hintereinander sind ein starkes KI-Signal.

Vorher:
> Zunächst wird das Konzept definiert. Anschließend werden zentrale Aspekte erläutert. Abschließend wird die Bedeutung diskutiert.

Nachher:
> Wir definieren erstmal das Konzept, besprechen dann die wichtigsten Punkte und schauen am Ende, was es eigentlich bedeutet.

Vorher (Nominalstil):
> Die Entwicklung von Lösungen erfolgt unter Berücksichtigung der Anforderungen.

Nachher:
> Wir entwickeln Lösungen, die zu den Anforderungen passen.

Fix: Passiv durch Aktiv ersetzen. Nominalisierungen zurück in Verben.

D10. Hedging-Konjunktiv statt klarer Aussagen.
Problem: KI stapelt "könnte", "würde", "möglicherweise", "potenziell" als Absicherung – oft mehrfach im selben Satz. Den synthetischen Konjunktiv II (wäre, käme, ließe sich), der natürliches Schriftdeutsch prägt, nutzt sie dagegen zu selten.

Vorher:
> Diese Maßnahme könnte möglicherweise dazu beitragen, die Effizienz potenziell zu steigern.

Nachher:
> Diese Maßnahme dürfte die Effizienz steigern. Sicher wissen wir es nach dem ersten Quartal.

Fix: pro Aussage höchstens eine Absicherung. Wo Konjunktiv gebraucht wird, auch mal die synthetische Form (ließe sich, wäre) statt der würde-Umschreibung.

D11. Wörtliche Übersetzungen aus dem Englischen.
Vorher:
> Sie nahm einen tiefen Atemzug. (She took a deep breath)
> Lassen Sie uns dem ins Gesicht sehen. (Let's face it)

Nachher:
> Sie atmete tief durch.
> Seien wir ehrlich.

Fix: wörtliche Übersetzungen durch natürliche deutsche Wendungen ersetzen.

D12. Fehlende regionale Färbung.
Problem: KI schreibt ausschließlich neutrales Hochdeutsch ohne jede regionale Färbung. Kein Österreichisch, kein Schweizerhochdeutsch, keine bayerischen oder norddeutschen Ausdrücke.
Fix: nur einstreuen, wenn die Vorlage schon regionale Färbung oder eine klar mündliche Stimme hat – dann reicht ein einzelnes "na ja" oder "gell?". Einem neutralen Text keine Region verpassen; das erfindet eine Person, die es nicht gibt.

D13. Orthographische Inkonsistenz.
Problem: KI hält innerhalb eines Textes keine einheitliche Schreibweise ein. "Onlineshops" und "Online-Shop" in aufeinanderfolgenden Sätzen.
Fix: eine Schreibweise wählen und durchhalten.

## Allgemeine Inhaltsmuster (14-42 gelten sprachübergreifend)

14. Überhöhte Bedeutungssprache.
Wörter: dient als, ist ein Beweis/Zeugnis für, eine entscheidende/zentrale Rolle, unterstreicht die Bedeutung, spiegelt breitere Trends wider

Vorher:
> Das Statistische Institut wurde 1989 gegründet, was einen entscheidenden Wendepunkt markierte.

Nachher:
> Das Statistische Institut wurde 1989 gegründet, um unabhängig regionale Statistiken zu erheben.

Fix: Tatsachen statt Pathos.

15. Werbesprache.
Wörter: lebendig, reich (bildlich), tiefgreifend, bahnbrechend, atemberaubend, renommiert, eingebettet in, nahtlos, innovativ, umfassend, ganzheitlich

Vorher:
> Eingebettet in die atemberaubende Region bietet die Stadt ein lebendiges kulturelles Erbe.

Nachher:
> Die Stadt ist bekannt für ihren Wochenmarkt und die Kirche aus dem 18. Jahrhundert.

Fix: überprüfbare Aussage statt Superlativ.

16. Vage Zuschreibungen.
Fix: Quelle benennen oder streichen. Hinterlässt das Streichen ein Loch, die Anpreisung durch eine ehrliche, zurückhaltende Selbstaussage ersetzen ("Perfekt ist es nicht, aber spürbar flüssiger als die letzte Version"), statt nichts dastehen zu lassen.

17. Notabilitäts-Politur.
Fix: Follower-Zahlen und Medienlisten nur behalten, wenn sie wirklich relevant sind.

18. Generische Zukunfts- oder Legacy-Sätze.
Fix: den konkreten Punkt stehen lassen und den Rest kappen.

19. Standardabschnitte wie "Herausforderungen und Chancen".
Fix: echte Probleme benennen.

## Sprachmuster

20. KI-Vokabular.
Hochfrequente KI-Wörter: innovativ, umfassend, ganzheitlich, präzise, bahnbrechend, effizient, nahtlos, eintauchen, auf ein neues Level heben, ermöglichen, nicht nur... sondern auch..., eine Vielzahl an, eine breite Palette an, darüber hinaus, zentral, facettenreich, Landschaft, unterstreichen, spannend, essenziell, maßgeblich, entscheidend, vielfältig, Meilenstein, eine Schlüsselrolle spielen

Vorher:
> Darüber hinaus bietet die innovative Plattform eine nahtlose, intuitive und umfassende Nutzererfahrung.

Nachher:
> Die Plattform ist einfach zu bedienen. Die Suche funktioniert schnell, die Navigation ist klar.

Fix: gewöhnliche Wörter bevorzugen.

21. Copula-Vermeidung.
Signal: steht für, dient als, markiert.
Fix: oft reicht "ist".

22. "Nicht nur ... sondern auch ..."
Vorher:
> Das Produkt bietet nicht nur eine intuitive Oberfläche, sondern auch leistungsstarke Analysefunktionen.

Nachher:
> Intuitive Oberfläche, starke Analyse. Beides gut.

Fix: direkt sagen, was gemeint ist.

23. Dreier-Listen und Adjektiv-Tripel.
Vorher:
> Die Lösung ist — sauber, effizient und ganzheitlich — ein großer Schritt nach vorn.

Nachher:
> Die Lösung funktioniert. Sauber und effizient.

Fix: auf ein starkes Wort oder eine konkrete Eigenschaft reduzieren.

24. Synonymhopping.
Fix: lieber das normale Hauptwort wiederholen als krampfhaft variieren.

25. Nominalisierung.
Fix: Nomen zurück in Verben verwandeln.

26. Hedge-Stapel.
Fix: Unsicherheit nur behalten, wenn sie sachlich nötig ist.

## Strukturmuster

27. Gleichförmige Satzlängen.
Vorher:
> Das neue Framework bietet signifikante Verbesserungen. Es umfasst bessere Fehlerbehandlung und umfangreichere Dokumentation. Nutzer werden die vereinfachte API schätzen.

Nachher:
> Das neue Framework ist besser. Deutlich besser. Die Fehlerbehandlung ergibt endlich Sinn, die Doku liest man vielleicht sogar freiwillig, und für die API braucht man keine 200-Zeilen-Config mehr.

Fix: Rhythmus öffnen.

28. Immer gleicher Satzanfang (eintöniges Vorfeld).
Problem: Deutsch ist eine V2-Sprache – vor dem finiten Verb kann fast jedes Satzglied stehen: Zeitangabe, Objekt, Adverbial. Menschen nutzen das ständig ("Den Bericht habe ich gestern gelesen"). KI besetzt das Vorfeld fast immer mit dem Subjekt.

Vorher:
> Das Team hat das Projekt rechtzeitig abgeschlossen. Der Kunde hat die Ergebnisse sofort genehmigt.

Nachher:
> Rechtzeitig fertig geworden, irgendwie. Der Kunde hat's sofort abgenickt – ohne eine einzige Änderung. Feier? Kurz. Dann weiter.

Fix: Einstiege variieren, solange die Klarheit bleibt. Auch mal Objekt oder Zeitangabe nach vorn stellen.

29. Zu viele und-Ketten.
Fix: kürzen, teilen oder unterordnen.

30. Jeder Absatz endet mit sauberer Minizusammenfassung.
Fix: manche Absätze auf Fakt, Bild oder Frage enden lassen.

31. Überall derselbe Registerton.
Fix: den Absätzen unterschiedliche Aufgaben geben.

32. Kommasetzung.
Problem: Deutsche Kommaregeln sind komplexer als englische. KI setzt zu wenige Kommas, besonders bei "dass"-Sätzen und erweiterten Infinitiven.

Vorher:
> Ich glaube dass dieser Ansatz funktioniert und wir ihn weiterverfolgen sollten.

Nachher:
> Ich glaube, dass dieser Ansatz funktioniert und dass wir ihn weiterverfolgen sollten.

Fix: Kommas vor Nebensätzen und Infinitivgruppen prüfen.

## Format- und Assistenzmuster

33. Fettdruck-Übernutzung und Doppelpunkt-Drama.
Problem: gestreuter Fettdruck als Betonungskrücke, und die Enthüllungs-Konstruktion "Nominalphrase: dramatische Pointe" ("Das Beste daran: es lernt von selbst.").
Fix: weniger hervorheben. Doppelpunkt-Enthüllungen als schlichte Sätze schreiben – Doppelpunkte gehören zu Listen, Etiketten und Zitaten, nicht zur Inszenierung.

34. Inline-Header-Listen.
Fix: in normale Sätze überführen, wenn das Format es nicht braucht.

35. Emoji-Dekoration.
Fix: in formellen Kontexten meistens entfernen.

36. Helfer-Sprache.
Signal: "lassen Sie uns eintauchen", "hier ist eine Aufschlüsselung"
Todesphrasen: Lassen Sie uns eintauchen, Es ist wichtig zu beachten, Es lässt sich nicht leugnen, Tauchen wir ein
Auch Pseudo-Einsicht-Auftakte: Was die meisten übersehen, Das sagt dir niemand, Was die meisten falsch machen, Die eigentliche Frage ist
Fix: näher am Inhalt starten. Pseudo-Einsicht-Auftakte streichen und die Behauptung allein stehen lassen.

37. Modell- oder Cutoff-Selbstkommentar.
Fix: löschen, wenn er nicht gebraucht wird.

38. Übertrieben zustimmender Ton.
Fix: nützlich und direkt formulieren.

## Kognitive Muster

39. Kein Denkprozess, aber der Text tut allwissend.
Vorher:
> Das Framework bietet eine umfassende Lösung für Datenmanagement.

Nachher:
> Das Framework macht Datenmanagement gut – nein, "gut" trifft's nicht ganz. Die Skalierbarkeit ist die eigentliche Story, wobei ich die Zuverlässigkeit noch länger testen würde.

Fix: bei informellen Texten etwas gedankliche Bewegung zulassen; sonst nüchtern bleiben.

40. Flacher Emotionsbogen.
Vorher:
> Die Entlassungen betrafen viele Mitarbeiter. Die Situation war für alle Beteiligten schwierig.

Nachher:
> 200 Leute haben am Dienstagmorgen in einem Zoom-Call ihren Job verloren. Manche waren seit zehn Jahren dabei. Die Abfindung war okay – aber "okay" macht einen 15-Minuten-Call, der zehn Jahre beendet, nicht besser.

Fix: nur dort Nuance hinzufügen, wo die Vorlage schon Haltung zeigt.

41. Zu berechenbare Wortwahl.
Vorher:
> Das Projekt wurde erfolgreich abgeschlossen und das Team feierte den Erfolg mit großer Begeisterung.

Nachher:
> Das Projekt ist raus. Gerade so. Wir haben Pizza bestellt und zwei Stunden aufs Monitoring-Dashboard gestarrt, in der Erwartung, dass irgendwas crasht. Nichts ist gecrasht. Das war die Feier.

Fix: das treffende Wort wählen, nicht das "schriftstellerischste".

42. Überkorrigierte "Menschlichkeit".
Problem: Wer jeden KI-Text mit denselben drei Tricks humanisiert, erzeugt eine neue, genauso erkennbare Schablone – Stakkato-Fragmente ("Kein Durchbruch. Nur ein Update."), inszenierte Selbstkorrekturen ("Moment – so stimmt das nicht"), pflichtschuldige rhetorische Fragen, "Seien wir ehrlich" in jedem zweiten Absatz, Modalpartikeln in jedem Satz.

Anzeichen: ein Fragment in jedem Absatz; mehr als eine Selbstkorrektur pro Text; zehn verschiedene Umschreibungen, die alle im selben schnoddrigen Rhythmus enden.

Fix: pro Text zwei bis drei Eingriffe wählen und die Mittel von Text zu Text wechseln. Das Ergebnis gegenlesen: Hat es jetzt eine gleichförmig "lockere" Stimme, die die Vorlage nie hatte, zurück Richtung Originalregister drehen.

## Kalibrierung: Wie viel ist genug

Zu viel umzuschreiben ist der häufigste Fehler. Die meisten echten Texte brauchen eine Handvoll Eingriffe, keine Generalüberholung.

Beispiel – diese Vorlage ist schon weitgehend in Ordnung:
> Die Migration hat drei Wochenenden gedauert statt einem. Die meiste Zeit ging für den Auth-Service drauf, den seit 2019 niemand angefasst hatte. Am Ende lag das Problem in einer Config-Datei, die die Staging-Umgebung überschrieb.

Eine Komplettkur wäre hier falsch. Vertretbar sind nur Kleinigkeiten: vielleicht zwei Sätze verbinden, vielleicht ein Wort straffen. Wenn du nicht benennen kannst, welches Muster ein Satz verletzt, lass den Satz stehen.

Faustregel: Bei einem Text, der schon natürlich klingt, unter 20 Prozent der Sätze anfassen.

## Domain-Hinweise

E-Mail:
- kurz und natürlich
- Grußformeln nicht mechanisch wiederholen

Blog / Essay:
- Stimme darf stärker hörbar sein
- keine erfundenen Anekdoten

Technische Doku:
- Präzision vor Stil

Geschäft:
- konkrete Angaben vor Pose
- echte Zahlen, echte Namen

Akademisch / behördlich:
- Formalität wahren
- keine erzwungene Lockerheit

## Anti-Halluzinations-Regel

Nicht hinzufügen:
- erfundene Kennzahlen oder Statistiken
- Meetings, Gespräche oder Anekdoten, die nie im Text standen
- neue Firmennamen, Städte oder Produkte
- ein Ich-Erlebnis, das nicht belegt ist

## Quellen

Deutschspezifisch:
- ADVERTEXT Lektoratstest — Komposita, Kasus, Orthographie
- Kathrin Landsdorfer — 21 ChatGPT-Phrasen im Deutschen
- ContentConsultants — KI-Texte erkennen
- WORTLIGA — KI-Texte humanisieren (Konjunktiv-Empfehlung)
- literaturcafe.de — Gedankenstrich-Analyse
- fyrfeed — 4 klare Hinweise auf KI-Text
- Leemeta Übersetzungen — 5 typische ChatGPT-Fehler im Deutschen
- KONVENS 2024, Irrgang et al. — "Features and Detectability of German Texts Generated with LLMs"
- De Gruyter 2025 — ChatGPT vs. DeepSeek vs. L1/L2 Deutsch

Allgemein:
- Wikipedia "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Tercon & Dobrovoljc (2025) — 44-Studien-Synthese
- Reinhart et al. (2024) — modellspezifische Syntaxsignaturen
- Herbold et al. (2023) — Nominalisierung und Funktionswörter
- Opara (2025) — fehlende Selbstkorrektur
- Alsadhan (2026) — Perplexitätsuniformität
