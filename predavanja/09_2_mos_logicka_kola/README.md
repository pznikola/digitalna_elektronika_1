# Logička kola sa MOS tranzistorima — 2. deo

Izvor: `../09 2 MOS logicka kola.pdf`, 31 PDF strana i 62 slajda.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Redizajn po PLAN_PREDAVANJA.md: **62/62 slajda i beleške obrađeni**, bez promene broja, redosleda ili ID-jeva; stil B, tema etf-v1. Status **u_radu**: 16 grupa stručnih predloga čeka korisnikovu odluku. Ranije završena rekonstrukcija nije odobrenje redizajna.

- [Prezentacija](build/09_2_mos_logicka_kola.pdf)
- [Beleške za predavača](build/09_2_mos_logicka_kola_beleske.pdf)
- [Uporedni pregled](build/redizajn/pregled/index.html)
- [Izveštaj i nastavak rada](provera/redizajn/izvestaj.md)
- [P01–P16 za odluku](provera/redizajn/otvorena_pitanja.md)

Iz korena repozitorijuma:

```sh
make -C predavanja LECTURE=09_2_mos_logicka_kola all
make -C predavanja LECTURE=09_2_mos_logicka_kola notes
make -C predavanja LECTURE=09_2_mos_logicka_kola review
make -C predavanja LECTURE=09_2_mos_logicka_kola check
python3 predavanja/09_2_mos_logicka_kola/kodovi/provera_redizajna.py
```

Kompilacija prolazi. Postojeća skripta izvršava 179, dopunska 24 računska poređenja. `check` prijavljuje samo 50 otvorenih stručnih kategorija; izvorne nedoslednosti ostaju do odobrenja. Originalni PDF i istorijska evidencija `provera/uocene_greske.md`/`provera/pregled.json` nisu promenjeni. Početni prikaz ima trajnu arhivu u `provera/redizajn/pocetni_prikaz.tar.gz`.
