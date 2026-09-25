# Elementi analize logičkih kola

Izvor: `../08 Elementi analize logickih kola.pdf`, 34 PDF strane i 67 slajdova.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Svih **67/67 slajdova** rekonstruisano je i pojedinačno sadržinski i vizuelno pregledano.

```sh
make -C predavanja LECTURE=08_elementi_analize_logickih_kola all
make -C predavanja LECTURE=08_elementi_analize_logickih_kola check
make -C predavanja LECTURE=08_elementi_analize_logickih_kola review
```

Izlaz: `build/08_elementi_analize_logickih_kola.pdf`. Šeme, karakteristike prenosa,
vremenski dijagrami i RC/RL odzivi imaju uređive TikZ izvore. Kataloške tabele
su tekstualni LaTeX. Kvalitativni grafikoni ostaju kvalitativni.
`kodovi/provera_logike.py` koristi samo standardnu Python biblioteku i proverava
računske odnose, kontinuitet i ekvivalentne izraze odziva. Greške originala su
sačuvane u prezentaciji i opisane u `provera/uocene_greske.md`.
