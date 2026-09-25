# Status prenosa — 04

Rekonstruisano i pojedinačno sadržinski i vizuelno pregledano: **39/39 slajdova**.
Original ima 20 PDF strana; poslednja ima samo gornji slajd. Izlaz ima 39 Beamer strana.
Sve formule, tabele, registri, magistrale, strelice i oznake poništavanja imaju uređive izvore.
Sačuvani su svi međukoraci, ponavljanja i izvorna isticanja cifara.

Završna komanda prolazi:
`make -C predavanja LECTURE=04_brojni_sistemi check`.
Nema prekoračenja prostora, nedostajućih znakova ni nerešenih referenci.
Potvrde svih kategorija i kontrolne sume prikaza nalaze se u `pregled.json`.

Nezavisna provera čita ćelije tabela deljenja, množenja, osnova i kodova negativnih
brojeva. Tačnom racionalnom aritmetikom proverava konverzije i fiksnu tačku.
Neskladi originala uključuju zaokruženu poslednju decimalu na slajdu 6, nestrogu
nejednakost na slajdu 9 i nedostajuće zagrade na slajdu 35. Sadržaj ostaje verno
prenesen; obrazloženja i predlozi nalaze se u `uocene_greske.md`.
