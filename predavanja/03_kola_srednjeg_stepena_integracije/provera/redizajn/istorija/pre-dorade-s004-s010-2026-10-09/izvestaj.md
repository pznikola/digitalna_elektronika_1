# Izveštaj 03 — terminologija slajdova i beleške

## Aktuelni status — 2026-10-09

**Status: `ceka_odobrenje`.** Završena je korisnikom odobrena terminološka dorada slajda **03-s002**. Projekcija i A4 PDF beležaka imaju po **21 strana**; broj, redosled i stabilni ID-jevi ostaju isti. Tema je zamrznuta **etf-v1**, stil **B**.

Prezentacija 03 i nove beleške čekaju korisnikovo prihvatanje; ova terminološka odluka nije odobrenje cele prezentacije 03. Za ovu terminološku doradu nema otvorenih stručnih pitanja. Ranija odobrenja i zasebne dozvole za početak drugih predavanja ostaju u [odlukama](odluke.md) i centralnoj evidenciji.

## Odluka i izmene

Korisnikova stvarna poruka nakon liste tri pojavljivanja:

> zameni sve

Potom je izričito zatražena primena plana „Zamena termina „kapija“ u slajdovima“.

| Mesto | Pre | Posle |
|---|---|---|
| 03-s002, uvod | logičkih kapija | logičkih gejtova |
| 03-s002, zaglavlje tabele | Broj kapija | Broj gejtova |

Izmena je jezička i terminološka; značenje, formule, brojčane vrednosti, topologija šema i tekst izvora beležaka očuvani su. Interni nazivi LaTeX komandi i TikZ stilova ostali su isti. Originalni PDF i korišćena tema imaju nepromenjene otiske. Nije dodat ili uklonjen nastavni sadržaj, niti premeštan sadržaj između slajdova i beležaka.

[Mapa pokrivenosti](pokrivenost.md) i [inventar](inventar.json) obuhvataju **91/91 potvrđenih elemenata**. Ažurirani su opisi terminološke izmene za pogođene elemente. Detaljna obrada nastavnog teksta beležaka iz 2026-10-02 ostaje dokumentovana u [prethodnom izveštaju](istorija/pre-zamene-termina-2026-10-09/izvestaj.md) i [evidenciji beležaka](evidencija_beleski.json).

## Pregled i provere

Stvarno su pregledani novi projekcioni **03-s002** i njegova cela A4 strana, uz originalni i prethodni prikaz. Novi termini su čitljivi; nema preklapanja ili odsecanja. Nastavni tekst beležaka ostaje isti, a u njih je ugrađen novi prikaz slajda.

Za ostalih **20 slajdova** provereni su identični lokalni izvori, pokrivenost i pikselno isti projekcioni i A4 prikazi. Ranije sadržinske potvrde sačuvane su uz taj dokaz. Zajednički otisak izgradnje obnovljen je zbog ranije promenjenog alata `redizajn.py`; ovim zadatkom alat, tema i zajednički stilovi nisu menjani. Pogođena potvrda obnovljena je tek nakon pregleda. Dokazi su u [poređenju](poredjenje_terminologije_2026-10-09.json) i [potvrdama](pregled.json).

Sve sledeće komande završene su sa izlaznim kodom **0**:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
```

`check`: **PROVERENO**, uključujući postojeću računsku proveru. Potvrđeni su broj i redosled strana i ID-jeva u oba PDF-a, pokrivenost i aktuelnost potvrda. Završni LaTeX logovi nemaju greške, upozorenja, prekoračenja prostora ili nedostajuće znakove. U vidljivom tekstu ovog prezentacionog PDF-a više nema oblika reči „kapija“.

[Notes log](../../build/redizajn/zamena-terminologije-2026-10-09/notes.log), [review log](../../build/redizajn/zamena-terminologije-2026-10-09/review.log), [check log](../../build/redizajn/zamena-terminologije-2026-10-09/check.log).

## Isporuka i otisci

- [Prezentacija — 21 slajdova](../../build/03_kola_srednjeg_stepena_integracije.pdf)
- [PDF beležaka — 21 A4 strana](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf)
- [Uporedni pregled](../../build/redizajn/pregled/index.html#03-s002)
- [Sačuvani izvori i evidencija pre ove izmene](istorija/pre-zamene-termina-2026-10-09/izvori-i-evidencija.tar.gz)

Izlazi u `build/` ne verzionišu se; navedene komande obnavljaju ih iz izvora. Izvori i istorijska evidencija ostaju van tog foldera.

| Resurs | SHA-256 aktuelne verzije |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Manifest redizajna | `043cfd60fc37b3776983018ddca3b715e03d99d8c679ea1e8de9df4306469213` |
| Zapis izgradnje | `aee5fbaa05e12b1ba2ecdc312845e693f429c0a16c544c5a36dcab5c212e8e05` |
| Potvrde pregleda | `c106d9effa6ee56342e611aa00796ad4034058187c2a446d20431ae09e9def57` |
| Mapa pokrivenosti | `59eb8e6c8348633b7fc28a00a6138f57fee75b9764fa70165ec999d1e9ca8791` |
| Prezentacioni PDF | `ceaae78a96629972b8b61b2e10fc1c51ba989722e206ab81f153c43595d599c6` |
| PDF beležaka | `289c7be8bf05068ac271e99fd8f400450c7731c5de83b656c300f37787a85221` |
| Evidencija beležaka | `2a8318a532e68b33501629547b9dc3f7a1481169d1f30016b73337fb0e332deb` |
| Dokaz poređenja | `d5253b9d9aef1463ce423e188890f5bc813c5873686a7591e189795e7eca289d` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak rada

Odobrena terminološka izmena je završena i proverena. Status ostaje `ceka_odobrenje` za prihvatanje rezultata koje nije dato ovom porukom. Pri nastavku proveriti aktuelne otiske i preskočiti završenu analizu nepromenjenih izvora; naknadna izmena poništava samo pogođene potvrde. Ovaj zadatak obuhvata konkretne terminološke zamene u 01 i 03 i ne odobrava druge izmene.
