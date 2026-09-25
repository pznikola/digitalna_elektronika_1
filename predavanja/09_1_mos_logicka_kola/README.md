# Logička kola sa MOS tranzistorima — 1. deo

Izvor: `../09 1 MOS logicka kola.pdf`, 29 PDF strana i 57 slajdova.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Svih **57/57 slajdova** rekonstruisano je i pojedinačno sadržinski i vizuelno pregledano.

```sh
make -C predavanja LECTURE=09_1_mos_logicka_kola all
make -C predavanja LECTURE=09_1_mos_logicka_kola check
make -C predavanja LECTURE=09_1_mos_logicka_kola review
```

Izlaz: `build/09_1_mos_logicka_kola.pdf`. Simboli, mreže, tranzistorske šeme,
karakteristike i grafička isticanja imaju uređive TikZ izvore. Kvalitativne
krive ostaju kvalitativne. Sve formule i međukoraci napisani su u LaTeX-u.
`kodovi/provera_logike.py` koristi standardnu Python biblioteku i sprovodi 231
nezavisno računsko poređenje, kao i protivprimere grešaka originala.
Izvorne greške sačuvane su na slajdovima i navedene u `provera/uocene_greske.md`.
