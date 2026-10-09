# Izveštaj 01 — terminologija slajdova i beleške

## Aktuelni status — 2026-10-09

**Status: `ceka_odobrenje`.** Završena je korisnikom odobrena terminološka dorada slajda **01-s027**. Projekcija i A4 PDF beležaka imaju po **37 strana**; broj, redosled i stabilni ID-jevi ostaju isti. Tema je zamrznuta **etf-v1**, stil **B**.

Prethodno odobrenje „I approve 01“ ostaje vezano za tada pregledanu verziju. Nove beleške od 2026-10-02 i aktuelna isporuka čekaju korisnikovo prihvatanje. Za ovu terminološku doradu nema otvorenih stručnih pitanja. Ranija odobrenja i zasebne dozvole za početak drugih predavanja ostaju u [odlukama](odluke.md) i centralnoj evidenciji.

## Odluka i izmene

Korisnikova stvarna poruka nakon liste tri pojavljivanja:

> zameni sve

Potom je izričito zatražena primena plana „Zamena termina „kapija“ u slajdovima“.

| Mesto | Pre | Posle |
|---|---|---|
| 01-s027 | dve I kapije + invertor | dva I gejta + invertor |

Izmena je jezička i terminološka; značenje, formule, brojčane vrednosti, topologija šema i tekst izvora beležaka očuvani su. Interni nazivi LaTeX komandi i TikZ stilova ostali su isti. Originalni PDF i korišćena tema imaju nepromenjene otiske. Nije dodat ili uklonjen nastavni sadržaj, niti premeštan sadržaj između slajdova i beležaka.

[Mapa pokrivenosti](pokrivenost.md) i [inventar](inventar.json) obuhvataju **141/141 potvrđenih elemenata**. Ažurirani su opisi terminološke izmene za pogođene elemente. Detaljna obrada nastavnog teksta beležaka iz 2026-10-02 ostaje dokumentovana u [prethodnom izveštaju](istorija/pre-zamene-termina-2026-10-09/izvestaj.md) i [evidenciji beležaka](evidencija_beleski.json).

## Pregled i provere

Stvarno su pregledani novi projekcioni **01-s027** i njegova cela A4 strana, uz originalni i prethodni prikaz. Novi termini su čitljivi; nema preklapanja ili odsecanja. Nastavni tekst beležaka ostaje isti, a u njih je ugrađen novi prikaz slajda.

Za ostalih **36 slajdova** provereni su identični lokalni izvori, pokrivenost i pikselno isti projekcioni i A4 prikazi. Ranije sadržinske potvrde sačuvane su uz taj dokaz. Zajednički otisak izgradnje obnovljen je zbog ranije promenjenog alata `redizajn.py`; ovim zadatkom alat, tema i zajednički stilovi nisu menjani. Pogođena potvrda obnovljena je tek nakon pregleda. Dokazi su u [poređenju](poredjenje_terminologije_2026-10-09.json) i [potvrdama](pregled.json).

Sve sledeće komande završene su sa izlaznim kodom **0**:

```bash
make -C predavanja LECTURE=01_logicke_funkcije notes
make -C predavanja LECTURE=01_logicke_funkcije review
make -C predavanja LECTURE=01_logicke_funkcije check
```

`check`: **PROVERENO**, uključujući postojeću računsku proveru. Potvrđeni su broj i redosled strana i ID-jeva u oba PDF-a, pokrivenost i aktuelnost potvrda. Završni LaTeX logovi nemaju greške, upozorenja, prekoračenja prostora ili nedostajuće znakove. U vidljivom tekstu ovog prezentacionog PDF-a više nema oblika reči „kapija“.

[Notes log](../../build/redizajn/zamena-terminologije-2026-10-09/notes.log), [review log](../../build/redizajn/zamena-terminologije-2026-10-09/review.log), [check log](../../build/redizajn/zamena-terminologije-2026-10-09/check.log).

## Isporuka i otisci

- [Prezentacija — 37 slajdova](../../build/01_logicke_funkcije.pdf)
- [PDF beležaka — 37 A4 strana](../../build/01_logicke_funkcije_beleske.pdf)
- [Uporedni pregled](../../build/redizajn/pregled/index.html#01-s027)
- [Sačuvani izvori i evidencija pre ove izmene](istorija/pre-zamene-termina-2026-10-09/izvori-i-evidencija.tar.gz)

Izlazi u `build/` ne verzionišu se; navedene komande obnavljaju ih iz izvora. Izvori i istorijska evidencija ostaju van tog foldera.

| Resurs | SHA-256 aktuelne verzije |
|---|---|
| Originalni PDF | `0bfe99550e77b8985d47b80bcce3ffeb66a55f32dcf991690fe5c0e707c39f8a` |
| Manifest redizajna | `3a57a05629241a97a70e2ad9eff699cf46ae159c9ff66f36de643e6f2114411e` |
| Zapis izgradnje | `55dafad91de36158c2d88e0c98738f0325296732734cccb184308c84c5fcf02b` |
| Potvrde pregleda | `bb8a70e9b20277f2c439cdf3b9bca05abe0bcfe599ff738f4bbd3afc9f9e6631` |
| Mapa pokrivenosti | `b90520c1ee9fa088b894b382168e379ae9dc7fff39477b1e16969ed4dbfaacf5` |
| Prezentacioni PDF | `1c69bafda3965271b2a0b45526fe776b3faebc501d8ea7504f8bf1a64dc2902e` |
| PDF beležaka | `1cfbda51a3f6b52157cc6f01d77ac48d0218e98522c1bf2453c8f4fde1961bca` |
| Evidencija beležaka | `4f890edb13af24ecd58ceb874d0e2937aace8783f2a4fb86dea45ce0d86c9a43` |
| Dokaz poređenja | `3b3d9f08c771319819692009a7386d0ee6703cccc94348ad688ce91bd1bea4b8` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak rada

Odobrena terminološka izmena je završena i proverena. Status ostaje `ceka_odobrenje` za prihvatanje rezultata koje nije dato ovom porukom. Pri nastavku proveriti aktuelne otiske i preskočiti završenu analizu nepromenjenih izvora; naknadna izmena poništava samo pogođene potvrde. Ovaj zadatak obuhvata konkretne terminološke zamene u 01 i 03 i ne odobrava druge izmene.
