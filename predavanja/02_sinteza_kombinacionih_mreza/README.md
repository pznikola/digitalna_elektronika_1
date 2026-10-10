# 02 — Sinteza kombinacionih mreža

Original: `../02 Sinteza kombinacionih mreza.pdf`, 27 PDF strana i 54 izvorna slajda; Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac. Original i istorijska mapa ostaju neizmenjeni.

Aktuelna verzija od 2026-10-09 ima **65 projektovanih slajdova i 65 A4 strana**: 54 originala, osam ranije odobrenih nastavaka i tri odobrena RTL dodatka. Prethodna verzija sa 62 strane prihvaćena je 2026-10-05; [zapis njenog odobrenja](provera/redizajn/odobrenje_rezultata.json) ostaje neizmenjen. Novi rezultat ima status `ceka_odobrenje`.

[Prezentacija](build/02_sinteza_kombinacionih_mreza.pdf), [beleške](build/02_sinteza_kombinacionih_mreza_beleske.pdf), [uporedni pregled](build/redizajn/pregled/index.html), [aktuelni izveštaj](provera/redizajn/izvestaj.md).

| Izvorni ID | Dodatni RTL slajd / strana PDF-a | Primer |
|---|---|---|
| 02-s021 | 02-s021-rtl01 / 25 | [mreza_zp — zbir proizvoda](kodovi/primeri_sv/02-s021/README.md) |
| 02-s022 | 02-s022-rtl01 / 27 | [mreza_pz — proizvod zbirova](kodovi/primeri_sv/02-s022/README.md) |
| 02-s051 | 02-s051-rtl01 / 62 | [mreza_sa_hazardom — simulacioni model](kodovi/primeri_sv/02-s051/README.md) |

Svaki primer ima automatski testbench i **Testbench bez provere**, koji sadrži samo pobude, čekanja i snimanje VCD-a. Komande za simulaciju su u README-u svakog primera. Model s051 zadržava izvornu pretpostavku da kasni samo invertor; za T=5 ns studentska pobuda pokazuje lažnu nulu od 20 do 25 ns. [Prikaz iz stvarnog VCD-a](build/redizajn/systemverilog/s051_lazna_nula.png).

```sh
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza all
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check-sv
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

`check-sv` koristi lokalni Docker image ili instalirane Verilator/Icarus; `HDL_LOCAL=1` izričito bira lokalne alate. Izlazi su u `build/redizajn/systemverilog/`; generisani PDF/PNG/VCD/HTML i simulatorovi izlazi ne verzionišu se.

[Stvarni nalog za dodatke](provera/redizajn/odobrenje_rtl.json), [odluke](provera/redizajn/odluke.md) i [odobrenja ranijih podela](provera/redizajn/odobrenje_podela.json) odvojeni su od prihvatanja rezultata. [Poređenje](provera/redizajn/poredjenje_rtl_dodataka.json) potvrđuje da svih 62 prethodna slajda i tela njihovih A4 prikaza ostaju pikselno isti; na pomerenim A4 stranama menja se samo broj u podnožju.

Prethodni izvori, evidencija i izveštaj sačuvani su u [istoriji](provera/redizajn/istorija/pre-rtl-primera-2026-10-09/izvestaj.md), a tadašnji izlazi u `build/redizajn/pre-rtl-primera-2026-10-09/`. Ne ponavljati sadržinsku analizu neizmenjenih originalnih slajdova. Provera zavisnosti, odobrenja i pogođenih prikaza obavezna je pri sledećoj izmeni.
