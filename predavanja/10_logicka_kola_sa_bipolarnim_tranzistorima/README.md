# Logička kola sa bipolarnim tranzistorima

**Redizajn 2026-10-03: `u_radu`.** Pregledani su original, početni i novi prikazi
svih 96 slajdova i nastavne beleške. Raspored, vektorske šeme i beleške uređeni
su prema [planu](../../PLAN_PREDAVANJA.md), uz očuvane ID-jeve, broj i redosled.
Devetnaest grupa izvornih stručnih pitanja čeka odluku korisnika; ova radna
verzija još nije odobrena za konačnu nastavnu upotrebu.

Izvor: `../10 Logička kola sa bipolarnim tranzistorima.pdf` (48 PDF strana), neizmenjen.

Originalni materijal: Digitalna elektronika 1, 2021/22, Katedra za elektroniku,
prof. dr Lazar Saranovac. Koristi se verzionisana tema `etf-v1`, izabrani stil B
i tamnocrvena nastavna isticanja. Autorstvo i školska godina ostaju izvorni.

Iz korena repozitorijuma:

```sh
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima all
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima notes
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima check
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima review
```

- [Prezentacija](build/10_logicka_kola_sa_bipolarnim_tranzistorima.pdf)
- [A4 beleške uz ID, naslov i slajd](build/10_logicka_kola_sa_bipolarnim_tranzistorima_beleske.pdf)
- [Original / pre / posle / beleške](build/redizajn/pregled/index.html)
- [Izveštaj redizajna](provera/redizajn/izvestaj.md)
- [Otvorena pitanja P01–P19](provera/redizajn/otvorena_pitanja.md)
- [Rezultati provera](provera/redizajn/rezultati_provera.md)

`slajdovi` sadrži 96 zasebnih izvora uključenih eksplicitno u glavni `.tex`.
Šeme, grafikoni i tehnički pogledi kućišta su u `slike/tikz`; tabele su u `tabele`.
Fotografija DIP kućišta izdvojena je iz originala, sa beleškom o poreklu.
`kodovi/provera_logike.py` sadrži 1018 nezavisnih računskih provera.

`provera/mapa.json` vezuje svaki slajd za izvornu stranu i položaj.
`beleske/sNNN.tex` su jedini izvori dodatnog nastavnog teksta. Poreklo, odluke,
pokrivenost i otisci pregledanih izvora/prikaza su u `provera/redizajn/`.
`check` ostaje `NEZAVRŠENO` samo zbog otvorenih stručnih pitanja; uspešna
kompilacija i računski model nisu zamena za njihovo razrešenje.

[Izveštaj rekonstrukcije](provera/izvestaj.md), [ranije potvrde](provera/pregled.json)
i [ranije uočene greške](provera/uocene_greske.md) ostaju istorijski zapisi.
Njihovo „završeno“ ne znači da je ovaj redizajn odobren.
Generisani PDF i HTML nalaze se u `build` i ne verzionišu se.
