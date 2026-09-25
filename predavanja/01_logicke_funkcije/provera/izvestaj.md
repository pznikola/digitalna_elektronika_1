# Status prenosa — 01

Rekonstruisano i sadržinski i vizuelno pregledano: **37/37 slajdova**.

- Original: 19 PDF strana; poslednja strana ima samo gornji slajd.
- Izlaz: 37 Beamer strana, po jedna za svaki originalni slajd, istim redosledom.
- Sve funkcionalne tabele, formule i logički dijagrami imaju uređive izvore.
- Pregledani su svi originalni i novi slajdovi u punoj veličini; ispravljeni su
  problemi sa prelomom tabela, razmacima u šemama i prikazom tro-ulaznih simbola.
- Kompilacija prolazi bez prekoračenja prostora, nedostajućih znakova i
  nerešenih referenci. Nezavisna provera logike prolazi.
- Greške i nepreciznosti izvornog zapisa sačuvane su u prezentaciji i izdvojene
  u `uocene_greske.md`; nisu prećutno ispravljane.

Merodavni pojedinačni statusi, beleške i kontrolne sume pregledanih prikaza
nalaze se u `pregled.json`. Promena izgleda traži novi pregled pogođenih slajdova.
Ponovljiva završna komanda iz korena: 
`make -C predavanja LECTURE=01_logicke_funkcije check`.
