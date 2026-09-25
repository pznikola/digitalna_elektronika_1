# Status prenosa — 06

**30/30 slajdova** sadržinski i vizuelno pregledano, jedan prema jedan.
Izvor: 15 PDF strana sa po dva slajda; izlaz: 30 Beamer strana.
Svaki slajd ima zaseban smisleno imenovan izvor i aktuelne kontrolne sume pregleda.

Provereni su svi tekstovi, formule, ćelije, boje, strelice i vremenske oznake.
Tabele ASCII/BCD/Grejovog koda, računskih međukoraka i zaštitnih kodova
ponovo su složene; vremenski dijagrami i Karnoove putanje nacrtani su u TikZ-u.

`kodovi/provera_logike.py` proverava ASCII pozicije, 40 BCD kodova,
komplemente, tri BCD računa, konverziju 243 i svih osam Shift-and-Add-3 koraka,
binary32 primere, 20 rezultata zaokruživanja, specijalne kodove,
Grejove cikluse, parnost svih 16 obrazaca greške, polinomski CRC i sve njegove
međukorake. Matematički ispravni skraćeni Hemingov (13,9) kod proverava se za
512 poruka i 13 pojedinačnih kvarova po poruci. Izvorne tabele imaju dodatni
pogrešan x u redu r₁/p₁, koloni 13: on je zasebno identifikovan i verno prenet;
provera ne predstavlja tvrdnju da je takva izvorna matrica ispravna.

Nalazi originala, uključujući FPF zapise, inverznu Grejovu konverziju i dodatni x,
odvojeni su od provere vernosti u `uocene_greske.md`. Nisu prećutno ispravljeni.
