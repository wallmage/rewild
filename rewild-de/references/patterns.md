# Rewild-DE Musterkatalog

Erst `SKILL.md` lesen. Diese Datei ist die Nachschlagehilfe für Diagnosen und Umschreibungen.

Hinweis: Die Vorher/Nachher-Paare unten sind Lehrbeispiele, die jedes Muster illustrieren. Das "Nachher" zeigt gutes menschliches Deutsch für dieses Muster, nicht eine wortwörtliche Umschreibung des "Vorher"-Textes. Beim echten Umschreiben nur Details verwenden, die bereits im Ausgangstext stehen.

## Höchste Priorität: deutschspezifische Muster

D1. Fehlende Modalpartikeln (stärkstes deutsches KI-Merkmal).
Problem: Modalpartikeln wie doch, halt, mal, eben, ja, schon, wohl, eigentlich, übrigens sind fundamental für natürliches Deutsch. Sie vermitteln Sprecherhaltung, mildern Aussagen, drücken Überraschung aus. KI benutzt sie fast nie, weil sie kein semantisches Eigengewicht haben und nicht ins Englische übersetzbar sind.

Vorher:
> Das ist richtig. Dieser Ansatz funktioniert. Wir sollten weitermachen.

Nachher:
> Das stimmt ja eigentlich. Der Ansatz funktioniert halt. Wir sollten mal weitermachen, oder?

Fix: in informellem Text natürlich einsetzen. Nicht in jeden Satz, aber da wo der Tonfall es braucht. In formellen Texten nicht erzwingen.

D2. Geviertstrich statt Halbgeviertstrich.
Problem: Englisch nutzt den Geviertstrich (—), Deutsch den Halbgeviertstrich (–) mit Leerzeichen beidseitig. KI setzt Geviertstriche in deutschen Text.

Vorher:
> Die Ergebnisse—sauber, effizient und ganzheitlich—sprechen für sich.

Nachher:
> Die Ergebnisse – sauber und effizient – sprechen für sich.

Fix: jeden — durch – mit Leerzeichen ersetzen.

D3. Falsche Anführungszeichen.
Problem: Deutsche Anführungszeichen öffnen unten (,,) und schließen oben (""). KI setzt englische ("...").

Vorher:
> Er sagte: "Das stimmt."

Nachher:
> Er sagte: ,,Das stimmt."

Fix: alle englischen durch deutsche ersetzen.

D4. Nebensatz-Wortstellung (Verb am Ende).
Problem: Im deutschen Nebensatz steht das konjugierte Verb am Ende. KI stellt es manchmal zu früh. Breiter: KI vermeidet komplexe Nebensätze ganz.

Vorher:
> Ich bin müde, weil ich habe schlecht geschlafen.

Nachher:
> Ich bin müde, weil ich schlecht geschlafen habe.

Fix: Nebensatz-Wortstellung prüfen. Auch bewusst komplexere Strukturen einbauen.

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

D7. Formelhafte Eröffnungen.
Todesphrasen: In der heutigen Zeit ist es wichtiger denn je..., In einer Welt, in der..., Im digitalen Zeitalter..., Immer mehr Menschen fragen sich..., Seit jeher...

Vorher:
> In der heutigen Zeit ist es wichtiger denn je, sich mit künstlicher Intelligenz auseinanderzusetzen.

Nachher:
> Letzten Monat hat mein Chef ChatGPT unsere Quartalszahlen zusammenfassen lassen. Das Ergebnis las sich wie eine Laudatio auf eine Firma, die es gar nicht gibt.

Fix: mit einer Anekdote, Szene, Frage oder konkretem Beispiel anfangen. Nie mit "In der heutigen Zeit."

D8. Kasus-Hyperkorrektheit.
Problem: KI übertreibt den Genitiv in Kontexten, wo natürliches Deutsch Dativ nutzen würde.

Vorher:
> Wegen des schlechten Wetters und des Kunde's Beschwerde wurde die Lieferung verschoben.

Nachher:
> Wegen dem schlechten Wetter und der Beschwerde des Kunden wurde die Lieferung verschoben.

Fix: Genitiv bei Präpositionen in informellem Text durch Dativ ersetzen (wegen dem, trotz dem). Schwache Maskulina korrekt deklinieren.

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

D10. Konjunktiv-Übernutzung (würde-Form).
Problem: KI übernutzt "könnte", "würde", "sollte" als Absicherung. Gleichzeitig nutzt sie den synthetischen Konjunktiv II (käme, gäbe, wäre) zu wenig.

Vorher:
> Man könnte argumentieren, dass diese Lösung würde helfen könnte.

Nachher:
> Diese Lösung hilft. Punkt. Ob sie auch langfristig trägt, ist eine andere Frage.

Fix: "könnte/würde/sollte" durch klare Aussagen ersetzen.

D11. Wörtliche Übersetzungen aus dem Englischen.
Vorher:
> Sie nahm einen tiefen Atemzug. (She took a deep breath)
> Lassen Sie uns dem ins Gesicht sehen. (Let's face it)

Nachher:
> Sie atmete tief durch.
> Seien wir ehrlich.

Fix: wörtliche Übersetzungen durch natürliche deutsche Wendungen ersetzen.

D12. Fehlende regionale Färbung.
Problem: KI schreibt ausschließlich Hochdeutsch ohne jede regionale Färbung. Kein Österreichisch, kein Schweizerdeutsch, keine bayerischen oder norddeutschen Ausdrücke.
Fix: wenn der Kontext es erlaubt, regionale Ausdrücke einstreuen. Nicht übertreiben — ein einzelnes "gell?" oder "na ja" reicht schon.

D13. Orthographische Inkonsistenz.
Problem: KI hält innerhalb eines Textes keine einheitliche Schreibweise ein. "Onlineshops" und "Online-Shop" in aufeinanderfolgenden Sätzen.
Fix: eine Schreibweise wählen und durchhalten.

## Allgemeine Inhaltsmuster (14-41 gelten sprachübergreifend)

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
Fix: Quelle benennen oder streichen.

17. Notabilitäts-Politur.
Fix: Follower-Zahlen und Medienlisten nur behalten, wenn sie wirklich relevant sind.

18. Generische Zukunfts- oder Legacy-Sätze.
Fix: den konkreten Punkt stehen lassen und den Rest kappen.

19. Standardabschnitte wie "Herausforderungen und Chancen".
Fix: echte Probleme benennen.

## Sprachmuster

20. KI-Vokabular.
Hochfrequente KI-Wörter: innovativ, umfassend, ganzheitlich, präzise, bahnbrechend, effizient, nahtlos, eintauchen, auf ein neues Level heben, ermöglichen, nicht nur... sondern auch..., eine Vielzahl an, eine breite Palette an, darüber hinaus, zentral, facettenreich, Landschaft, unterstreichen

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

28. Immer gleicher Satzanfang.
Vorher:
> Das Team hat das Projekt rechtzeitig abgeschlossen. Der Kunde hat die Ergebnisse sofort genehmigt.

Nachher:
> Rechtzeitig fertig geworden, irgendwie. Der Kunde hat's sofort abgenickt – ohne eine einzige Änderung. Feier? Kurz. Dann weiter.

Fix: Einstiege variieren, solange die Klarheit bleibt.

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

33. Fettdruck-Übernutzung.
Fix: weniger hervorheben.

34. Inline-Header-Listen.
Fix: in normale Sätze überführen, wenn das Format es nicht braucht.

35. Emoji-Dekoration.
Fix: in formellen Kontexten meistens entfernen.

36. Helfer-Sprache.
Signal: "lassen Sie uns eintauchen", "hier ist eine Aufschlüsselung"
Todesphrasen: Lassen Sie uns eintauchen, Es ist wichtig zu beachten, Es lässt sich nicht leugnen, Tauchen wir ein
Fix: näher am Inhalt starten.

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
