# Logička kola sa bipolarnim tranzistorima

**96/96 slajdova** rekonstruisano i pojedinačno provereno sadržinski i vizuelno.
Izvor: `../10 Logička kola sa bipolarnim tranzistorima.pdf` (48 PDF strana).

Originalni materijal: Digitalna elektronika 1, 2021/22, Katedra za elektroniku,
prof. dr Lazar Saranovac. Ponavljajući podaci i logo uklonjeni su sa novih slajdova.

Iz korena repozitorijuma:

```sh
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima all
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima check
make -C predavanja LECTURE=10_logicka_kola_sa_bipolarnim_tranzistorima review
```

- [Prezentacija](build/10_logicka_kola_sa_bipolarnim_tranzistorima.pdf)
- [Uporedni pregled](build/pregled/index.html)
- [Izveštaj provere](provera/izvestaj.md)
- [Uočene greške originala](provera/uocene_greske.md)

`slajdovi` sadrži 96 zasebnih izvora uključenih eksplicitno u glavni `.tex`.
Šeme, grafikoni i tehnički pogledi kućišta su u `slike/tikz`; tabele su u `tabele`.
Fotografija DIP kućišta izdvojena je iz originala, sa beleškom o poreklu.
`kodovi/provera_logike.py` sadrži 1018 nezavisnih računskih provera.

`provera/mapa.json` vezuje svaki slajd za izvornu stranu i položaj.
`provera/pregled.json` sadrži potvrde kategorija i kontrolne sume pregledanih prikaza.
Generisani PDF i HTML nalaze se u `build` i ne verzionišu se.
