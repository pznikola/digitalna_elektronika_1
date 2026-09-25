# Status prenosa — 03

Rekonstruisano i pojedinačno sadržinski i vizuelno pregledano: **21/21 slajd**.
Original ima 11 PDF strana; poslednja ima samo gornji slajd. Izlaz ima 21 Beamer stranu.
Sve šeme i tabele imaju uređive izvore. Delimično prazni crteži na originalnim slajdovima
6 i 12 preneti su kao takvi, bez dopunjavanja nastavnog sadržaja.

Završna komanda prolazi:
`make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check`.
Nema prekoračenja prostora, nedostajućih znakova ni nerešenih referenci.
Potvrde svih kategorija i kontrolne sume prikaza nalaze se u `pregled.json`.

Nezavisno su proverene tabele kodera prioriteta, dekoder i multiplekser 4/1,
svih 64 indeksa matričnog dekodera i svih 65.536 kombinacija ulaza kodera 16/4.
Nesklad tvrdnje o NI kolima i formule na slajdu 4 verno je prenet, uz računski
kontraprimer u proveri i odvojeni predlog ispravke u `uocene_greske.md`.
