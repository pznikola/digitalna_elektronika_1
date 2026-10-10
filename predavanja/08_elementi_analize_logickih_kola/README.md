# Elementi analize logičkih kola

Izvor: `../08 Elementi analize logickih kola.pdf`, 34 PDF strane i 67 slajdova.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Svih **67/67 slajdova** bilo je rekonstruisano i pregledano u prethodnoj fazi. Njene potvrde ne potvrđuju novi redizajn.

**Redizajn, 2026-10-03:** pregledano i uređeno svih 67 slajdova i njihovih A4 beležaka prema `PLAN_PREDAVANJA.md`, uz temu `etf-v1` i stil B. Broj i redosled su nepromenjeni. Kompilacija i računske provere prolaze; status je `u_radu`, jer 12 grupa stručnih predloga iz originala čeka korisnikovu odluku. `check` zato vraća `NEZAVRŠENO`. Vidi [izveštaj](provera/redizajn/izvestaj.md), [P01–P12](provera/redizajn/otvorena_pitanja.md), [prezentaciju](build/08_elementi_analize_logickih_kola.pdf), [A4 beleške](build/08_elementi_analize_logickih_kola_beleske.pdf) i [uporedni pregled](build/redizajn/pregled/index.html).

```sh
make -C predavanja LECTURE=08_elementi_analize_logickih_kola all
make -C predavanja LECTURE=08_elementi_analize_logickih_kola notes
make -C predavanja LECTURE=08_elementi_analize_logickih_kola check
make -C predavanja LECTURE=08_elementi_analize_logickih_kola review
```

Izlaz: `build/08_elementi_analize_logickih_kola.pdf`. Šeme, karakteristike prenosa,
vremenski dijagrami i RC/RL odzivi imaju uređive TikZ izvore. Kataloške tabele
su tekstualni LaTeX. Kvalitativni grafikoni ostaju kvalitativni.
`kodovi/provera_logike.py` koristi samo standardnu Python biblioteku i proverava
računske odnose, kontinuitet i ekvivalentne izraze odziva. Stručne greške originala su
sačuvane do odluke; istorijska zapažanja su u `provera/uocene_greske.md`, a aktuelni predlozi i status u `provera/redizajn/otvorena_pitanja.md`.
