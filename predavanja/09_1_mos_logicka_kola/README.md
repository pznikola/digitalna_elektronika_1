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


## Redizajn i beleške — 2026-10-03

Prethodna potvrda 57/57 odnosi se na rekonstrukciju. Sadašnji redizajn ima status **u_radu**: svih 57 slajdova i nastavne beleške uređeni su i pregledani, 284/284 sadržajna elementa ima odredište. Izgrađeni su prezentacioni PDF i poseban A4 PDF za predavača. `all`, `notes` i `review` prolaze, računska provera ima 231 uspešno poređenje; `check` ostaje NEZAVRŠENO u 22 kategorije zbog 13 grupa izvornih stručnih pitanja. Njihove ispravke nisu odobrene.

- [Izveštaj](provera/redizajn/izvestaj.md)
- [Predlozi za odluku P01–P13](provera/redizajn/otvorena_pitanja.md)
- [Beleške u PDF-u](build/09_1_mos_logicka_kola_beleske.pdf)
- [Uporedni pregled](build/redizajn/pregled/index.html)

```sh
make -C predavanja LECTURE=09_1_mos_logicka_kola notes
```

Sledeći agent nastavlja od stručnih odluka u izveštaju i potvrda `provera/redizajn/pregled.json`; završene analize ne ponavlja ako otisci nisu promenjeni. Nema odobrenja rezultata ili početka 09_2.
