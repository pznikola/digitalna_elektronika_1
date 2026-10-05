# Predavanje 02 — dodatna dorada s036/s037/s040

**Status: `ceka_odobrenje` · 2026-10-04.** Tražene dopune i raspored su završeni; sve provere prolaze, nema otvorenih stručnih pitanja. Korisnikov nalog odobrava doradu, a ne prihvatanje gotove prezentacije.

## Obuhvat i verzija

Original ostaje neizmenjen: 27 PDF strana i 54 izvorna slajda. Prezentacija i prateće beleške imaju po **60 strana**, uz ranije izričito odobrene nastavke s002b/s009b/s015b/s023b/s024b/s032b. Broj, redosled i stabilni ID-jevi nisu menjani ovom doradom. Stil B, zamrznuta tema etf-v1, fontovi, LuaLaTeX, odnos 16:9, autorstvo i školska godina 2021/22 su očuvani. Funkcije i indeksi polja nisu menjani; ranije odobren redosled zaglavlja A=0,1 nad C=1 ostaje ispravan.

## Izmene

| ID / PDF strana | Rezultat |
|---|---|
| s036 / 42 | Izričito objašnjeno da susedna polja imaju Hemingovo rastojanje 1, odnosno razlikuju se u tačno jednom bitu. Karta i oba niza susednih parova preko ivica ostaju vidljivi; dve kolone omogućavaju čitljiv tekst bez smanjivanja fonta. |
| s037 / 43 | Potpunije izvorno objašnjenje: pored susedstva unutar karata, susedna su i odgovarajuća polja pri preklapanju dve karte u 3D prostoru, na primer 0/16 i 1/17. |
| s040 / 46 | Vraćena izvorna logika uvoda, preklapanja i pravilnih površina. Jedna karta za tri promenljive jasno je izjednačena sa dve karte za C=0/1, uz jednake kvadratne ćelije 4.5 mm, poravnanje i potpune oznake. Donje dve celine objašnjavaju susedne parove 0/4, 1/5 i pravilne površine prvog reda 0/4 i drugog reda 0/1/4/5, uz označene odgovarajuće ćelije. Indeksi 7 pt prate lokalni stil prethodnih karata; ostale oznake 9 pt. |

[Uporedni pregled originala, polaznog prikaza, novog slajda i beležaka](../../build/redizajn/pregled/index.html). Neposredno prethodni prikazi sa 60 strana sačuvani su u `build/redizajn/pre-dorada-s036-s040-2026-10-04/`; izvori i evidencija u `istorija/pre-dorade-s036-s040-2026-10-04/izvori-i-evidencija.tar.gz`. [Prethodni izveštaj](istorija/pre-dorade-s036-s040-2026-10-04/izvestaj.md) čuva detalje ranijih dorada i tadašnje otiske; nije prepisan novim značenjem.

## Beleške i pokrivenost

**222/222 elemenata** ima provereno odredište: 163 izvorne grupe i 59 dopuna; 112 elemenata povezano je sa beleškama. Broj elemenata nije promenjen; dopunjeni su opisi postojećih izvornih celina i provera odredišta.

S036 beleške prenose izvorno objašnjenje zamišljenog presavijanja oko vertikalne i horizontalne ose, uz postojeće dodatno tumačenje indeksiranja, promene jednog bita i ugaone grupe. S037 sada vidljivo prikazuje izvorno preklapanje; njegov tekst beležaka ostaje nepromenjen i razjašnjava binarni odnos slojeva i uklanjanje E. S040 beleške zadržavaju dodatno objašnjenje indeksiranja i proizvoda grupa; uklonjena je jedna rečenica koja je ponavljala sada jasno vidljiv sadržaj. Nema uredničke evidencije, porekla PDF strana, korisnikovih odluka ili nepotrebnog prepisivanja slajda u nastavnim beleškama.

[Mapa pokrivenosti](pokrivenost.md), [evidencija beležaka](evidencija_beleski.json) i [odluke](odluke.md) dokumentuju poreklo i proveru izvan nastavnog PDF-a. Preformulisan je izvorni nastavni tekst bez stručnih promena; ispravljene su samo očigledne jezičke formulacije „1.og/2.og“ u „1. reda/2. reda“ i „Tabelu sa 3 promenljive“ u „kartu sa tri promenljive“.

## Provera i dokazi

Originali, lokalni izvori, konačni projekcioni prikazi i cele A4 beleške za **s036/s037/s040** stvarno su pregledani. Provereni su svi indeksi, oznake bitova, grupe, čitljivost, razmaci i odsustvo preklapanja i odsecanja.

[Poređenje](poredjenje_dorade_s036_s040.json) potvrđuje pikselnu jednakost **svih ostalih 57 celih slajdova i A4 strana**, uključujući podnožje. Njihove ranije potvrde i svi otisci ostaju važeći i neizmenjeni. Tri pogođene potvrde obnovljene su tek posle stvarnog pregleda. Originalni PDF i istorijska mapa nisu menjani. Provereno je 26 parova indeksa na Hemingovom rastojanju 1, uz značenje oba primera pravilnih površina.

Izvršeno sa izlaznim kodom 0:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

**`check`: PROVERENO.** Strukturna, sadržinska i postojeća računska provera prolaze; oba konačna LaTeX loga nemaju prekoračenja prostora, upozorenja ili grešaka. Svi ID-jevi, redosled, 60 slajdova i 60 A4 strana su potvrđeni. Alati i zajednička tema nisu menjani.

[Notes log](../../build/redizajn/dorada-s036-s040-2026-10-04/notes.log), [review log](../../build/redizajn/dorada-s036-s040-2026-10-04/review.log), [check log](../../build/redizajn/dorada-s036-s040-2026-10-04/check.log).

## Isporuka i nastavak

- [Prezentacija — 60 slajdova](../../build/02_sinteza_kombinacionih_mreza.pdf), pogođene strane 42, 43 i 46.
- [PDF beležaka — 60 A4 strana](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

Generisani PDF/PNG/HTML fajlovi i logovi u `build/` ne verzionišu se i obnavljaju gornjim komandama. Sledeći korak je korisnikov pregled ove verzije 02; rezultat nije odobren. Ranije dozvole za druga predavanja ostaju odvojene i nisu menjane.

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `105176bc1064d3f14928306747be1c7e832a6e9df6b78762ad1ac1d352c1053c` |
| Prezentacioni PDF | `c4de61bceff3eb301f60ff7e8cef01b3e9292059db44ab5f972b57cdab4401bd` |
| PDF beležaka | `9eac2628fc22753f0552aca9f5f0ff8467c2206df948ada4399ea27f2a06dfd6` |
| Zapis izgradnje | `5fc862c791ee988f82cec816b1f1d4dc7a12c45627f3d2a90c093c7c087d2f8d` |
| Potvrde pregleda | `22473d76144b3f4d8f4210a8b305a41130e318cca82cb3c293499078702d58ed` |
| Evidencija beležaka | `fbb00cfc8154ac6e1940ad471766a539ce9646ec11e0e989eba7bb509d51c7e0` |
| Poređenje prikaza | `998129d6aed5a6885a7a5b80122ecfa03ba06f87ef2d3673dc9b00938e26f978` |
| Arhiva prethodne isporuke | `b1304a0c80428b225051479c5155859d92297191fae28e965caaf3e3299bd28d` |
