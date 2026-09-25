# Status prenosa — 05

Rekonstruisano i pojedinačno sadržinski i vizuelno pregledano: **55/55 slajdova**.
Original ima 28 PDF strana; poslednja ima samo gornji slajd. Izlaz ima 55 Beamer strana.
Svi komparatori, sabirači, dijagrami toka, grafikoni, bitovne tabele i pseudokod
imaju uređive izvore. Sačuvani su svi međukoraci i namerno netačni primeri.

Završna komanda prolazi:
`make -C predavanja LECTURE=05_aritmeticke_operacije check`.
Nema prekoračenja prostora, nedostajućih znakova ni nerešenih referenci.
Potvrde svih kategorija i kontrolne sume prikaza nalaze se u `pregled.json`.

Nezavisne provere obuhvataju komparatore, sve redove tabela polusabirača i
potpunog sabirača, 512 ADD/SUB kombinacija sa OVF, sve osmobitne INC/DEC
ulaze, ćelije sedam tabela proizvoda, Boothovu jednakost za širine 2–8,
svih deset prikazanih stanja iterativnog primera, granice greške odsecanja
i količnik/ostatak iz stvarnih tabela deljenja.

Greške i sporni zapisi originala posebno su dokumentovani u `uocene_greske.md`.
To uključuje red prenosa na slajdu 14, nedosledni dodatak na slajdu 24,
obrnute krajnje prenose na slajdu 26 i zapis uslova na slajdovima 53–54.
Sadržaj prezentacije nije ispravljen u odnosu na original.
