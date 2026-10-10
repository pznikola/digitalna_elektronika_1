# Rezultati provera — 10, 2026-10-03

Status: `u_radu`. Kompilacija i struktura prolaze; stručni pregled ostaje otvoren.

| Provera | Rezultat |
|---|---|
| `all` (LuaLaTeX) | Uspešno; tačno 96 prezentacionih strana |
| `notes` (LuaLaTeX) | Uspešno; 96 A4 strana za 96 ID-jeva, sa slajdom i naslovom |
| `review` | Uspešno; original / početni / novi slajd / beleške za svih 96 ID-jeva |
| Broj, redosled, stabilni ID-jevi | Očuvani `10-s001`–`10-s096`; nema dodatnih overlay strana |
| Pokrivenost | 348/348 elemenata ima provereno odredište; 318 izvornih grupa i 30 dopuna |
| Odredišta beležaka | 105 grupa, povezane sa beleškama istog ID-ja |
| Kompilacijski logovi | Bez Overfull/Underfull, LaTeX/Package upozorenja i grešaka |
| Računski model | 1018 nezavisnih provera prošlo; nije potvrda tačnosti svakog izvornog izraza |
| Pojedinačni vizuelni pregled | Svih 96 originalnih, početnih i novih slajdova i A4 beleške pregledani |
| `check` | Očekivano `NEZAVRŠENO`: 26 stručnih kategorija na 20 ID-jeva, vezanih za 19 grupa P01–P19 |
| Strukturne greške, zastarele potvrde, nedostajući resursi/odredišta | Nema nalaza |

Komande iz korena repozitorijuma:

```bash
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima all
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima notes
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima review
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima check
python predavanja/10_logicka_kola_sa_bipolarnim_tranzistorima/kodovi/provera_logike.py
```

`review` i `check` ponovo grade aktuelne PDF-ove. Poslednji `check` vratio je
kod 1; make ga prenosi kao neuspešan cilj. Ovo ne označava kvar izgradnje.
Zadržane stručne kategorije su `problem`, a ne lažno potvrđene.
Pojedinačni otisci izvora/prikaza/beležaka su u [pregled.json](pregled.json),
a zavisnosti izgradnje u [izgradnja.json](izgradnja.json).

Svi preostali nalazi `check`:

- 10-s006/beleske: pregled nije potvrđen.
- 10-s014/formule: pregled nije potvrđen.
- 10-s030/formule: pregled nije potvrđen.
- 10-s030/beleske: pregled nije potvrđen.
- 10-s032/formule: pregled nije potvrđen.
- 10-s034/crtezi: pregled nije potvrđen.
- 10-s035/formule: pregled nije potvrđen.
- 10-s036/formule: pregled nije potvrđen.
- 10-s038/beleske: pregled nije potvrđen.
- 10-s058/formule: pregled nije potvrđen.
- 10-s059/formule: pregled nije potvrđen.
- 10-s060/formule: pregled nije potvrđen.
- 10-s065/formule: pregled nije potvrđen.
- 10-s065/beleske: pregled nije potvrđen.
- 10-s066/formule: pregled nije potvrđen.
- 10-s066/beleske: pregled nije potvrđen.
- 10-s078/tabele: pregled nije potvrđen.
- 10-s083/beleske: pregled nije potvrđen.
- 10-s084/formule: pregled nije potvrđen.
- 10-s084/beleske: pregled nije potvrđen.
- 10-s085/beleske: pregled nije potvrđen.
- 10-s090/formule: pregled nije potvrđen.
- 10-s090/beleske: pregled nije potvrđen.
- 10-s092/formule: pregled nije potvrđen.
- 10-s092/beleske: pregled nije potvrđen.
- 10-s093/crtezi: pregled nije potvrđen.

Za konkretna obrazloženja i predložene ispravke vidi [P01–P19](otvorena_pitanja.md).
