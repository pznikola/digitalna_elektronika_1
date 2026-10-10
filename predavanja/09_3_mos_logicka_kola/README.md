# Logička kola sa MOS tranzistorima — 3. deo

Izvor: `../09 3 MOS logicka kola.pdf`, 36 PDF strana i 71 slajd.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Svih **71/71 slajdova** rekonstruisano je i pojedinačno sadržinski i vizuelno
pregledano u prethodnoj fazi. Tadašnja potvrda rekonstrukcije ne potvrđuje
redizajn; aktuelno stanje je navedeno ispod.

```sh
make -C predavanja LECTURE=09_3_mos_logicka_kola all
make -C predavanja LECTURE=09_3_mos_logicka_kola check
make -C predavanja LECTURE=09_3_mos_logicka_kola review
```

Prezentacioni PDF: `build/09_3_mos_logicka_kola.pdf`. Svi crteži i tabele imaju
uređive izvore. `kodovi/provera_logike.py` izvršava 1007 nezavisnih računskih
provera. Njihov uspeh ne ispravlja greške originala: nalaze i predloge videti
u `provera/uocene_greske.md`. Dokaz vizuelnog pregleda je `provera/pregled.json`.

## Redizajn i beleške — 2026-10-03

Status **`u_radu`**. Svih 71 originalnih, početnih i novih slajdova i A4 beležaka pojedinačno je pregledano. Sačuvani su broj, redosled, ID-jevi i poreklo; korišćen je ETF `etf-v1`, stil B. Uređeni su raspored, 58 vektorskih izvora i nastavni tekst beležaka. Svih 304 elementa ima provereno odredište. Izvori dodatnih objašnjenja su u `beleske/sNNN.tex`, bez uredničkih komentara u prikazu.

- [Prezentacija](build/09_3_mos_logicka_kola.pdf)
- [PDF beležaka za predavača](build/09_3_mos_logicka_kola_beleske.pdf)
- [Uporedni pregled originala, početnog i novog prikaza sa beleškama](build/redizajn/pregled/index.html)
- [Izveštaj](provera/redizajn/izvestaj.md), [pokrivenost](provera/redizajn/pokrivenost.md) i [otvorena pitanja P01–P13](provera/redizajn/otvorena_pitanja.md)

Kompilacija i svih 1007 postojećih računskih provera prolaze. `check` trenutno vraća **NEZAVRŠENO** zbog 13 grupa stručnih pitanja iz originala (24 kategorije na 18 ID-jeva); nema strukturnih nalaza ni zastarelih potvrda. Stručne ispravke zahtevaju korisnikovu odluku prema `PLAN_PREDAVANJA.md`; nisu prećutno primenjene. Istorijska `provera/pregled.json` ostaje dokaz rekonstrukcije; aktuelne potvrde su u `provera/redizajn/pregled.json`. Rezultat 09_3 i početak 10 nisu odobreni.

```sh
make -C predavanja LECTURE=09_3_mos_logicka_kola notes
```

Posle odobrenih stručnih izmena obnoviti pogođene prikaze i potvrde, pa ponoviti `notes`, `review` i `check` za ovo predavanje. Sledeći agent nastavlja od evidentiranih pitanja, bez ponavljanja pregleda neizmenjenih izvora i njihovih zavisnosti.
