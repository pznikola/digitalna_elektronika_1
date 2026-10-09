# Izveštaj 03 — dorada s011–s015

## Status i verzija — 2026-10-09

**Status: `ceka_odobrenje`.** Dorada pet slajdova i njihovih beležaka je završena. Original i izvorna mapa imaju **21 slajd**; prezentacija i A4 beleške imaju po **22 strane**, uključujući ranije odobreni s010b. Redosled s001–s010 → s010b → s011–s021 i stabilni ID-jevi ostaju isti. Stil B, zamrznuta tema etf-v1, fontovi i autorstvo očuvani su.

[Stvarna korisnikova poruka](odluke.md) odobrava konkretnu doradu, dovršavanje s012 uz proveru na internetu i manji lokalni font s015. Nije prihvatanje cele prezentacije 03. Nema novih otvorenih stručnih pitanja.

## Tekst, raspored i dijagrami

| Slajd | Završena dorada |
|---|---|
| s011 | Vraćeni uvod o aktivnoj nuli na ulazima/izlazima, ekvivalentnost prva dva zapisa, najčešća upotreba drugog, posledica dvostruke negacije i opis unutrašnjeg CS signala. Šest simbola čuva sve priključke i negacije; niža geometrija oslobađa prostor za tekst. |
| s012 | Potpuna unutrašnja šema sa četiri I3 gejta i blokovski simbol DMUX 1/4 u stilu s008. Prikazani S1/S0/I, Y0–Y3, stvarne veze i tačke spojeva. Vraćeni zajednički kataloški naziv, identičnost sa dekoderom sa CS i postupak proširenja mreže. |
| s013 | Vraćeni posebna koderska mreža, obrnut smer od DMUX-a, prenos izabranog podatka i n/2^n/1 signala. Niža unutrašnja šema čuva sve ulaze, grane i spojne tačke. |
| s014 | Vraćeni poređenje sa dekoderom i princip izbora potpunih proizvoda. F je u jednom redu. Horizontalna strelica vodi od levog MUX-a ka desnom; dijagonalna počinje na F i pokazuje njenu realizaciju desnim MUX-om. Strelice ne presecaju blokove. |
| s015 | Vidljivi uvod prema originalu i objašnjenje stabla 16/1. Lokalni tekst 10/12 pt prema korisnikovoj dozvoli, oznake najmanje 9 pt. Osnovna šema i simbol su kompaktniji, a blokovi stabla širi radi razmaka teksta. |

Lokalni `mux_simbol.tex` sada prihvata dimenzije i veličinu oznaka; podrazumevani font ostaje 10/12 pt. Parametri su lokalni, a tema i alati nisu menjani. S015 nije skaliran kao celina.

Za s012 korišćena je [zvanična dokumentacija Nexperia 74HC238](https://assets.nexperia.com/documents/data-sheet/74HC_HCT238.pdf), Rev. 8, funkcionalni opis i tabela 3. Nenegirani nastavni DMUX 1/4 izveden je iz dokumentovanog 3/8 kola: E3 nosi I, E1/E2/A2 su nula, A1/A0 su selektori. Ovo je izvođenje nastavne šeme, a ne fizički pinout komponente. Aktivno niski podatkovni enable dao bi drugačiji polaritet. Poreklo i izvođenje zabeleženi su u [evidenciji](evidencija_beleski.json).

## Beleške i pokrivenost

[Mapa pokrivenosti](pokrivenost.md) ostaje sa **92/92 potvrđena elementa**: 71 izvornom grupom, 20 dopuna i jednim nastavkom postojeće dopune. Vraćeni izvorni tekst ne prepisuje se bez potrebe u beleške; ključne logičke celine ostaju vidljive.

Beleške s011 tumače aktivni izlaz i uslove CS; s012 daju četiri izlazne jednačine, primer adrese 10 i polaritete; s013 izraz MUX-a i razliku prema koderu; s014 uvrštavanje konstanti i dokaz Z=F; s015 uslovljeni izlaz, indeks 4g+k, primer I13 i lokalne/globalne oznake. Nema istorije dorade, zahteva za odobrenje ili uredničkih komentara. Poreklo, dokazi i nevidljiva sidra su u [evidenciji beležaka](evidencija_beleski.json).

## Pregled i provere

Stvarno su upoređeni originali, prethodni i konačni prikazi pet slajdova i pročitane njihove cele A4 strane. Proverena je svaka veza, negacija, spojna tačka, formula i oznaka. Nema preklapanja, odsecanja, nečitljivog teksta ili nepokrivenog sadržaja.

Ostalih **17 projekcionih i 17 celih A4 prikaza** pikselno je identično prethodnoj isporuci. Njihovi lokalni izvori i pokrivenost ostaju isti; prethodne sadržinske potvrde zadržane su uz [dokaz poređenja](poredjenje_dorade_s011_s015.json). Pet pogođenih potvrda obnovljeno je tek nakon pregleda. [Sve potvrde](pregled.json) odgovaraju aktuelnim izvorima i prikazima.

Završne komande završene su kodom **0**:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
```

`check`: **PROVERENO**, uz postojeće računske provere dekodera/MUX-a i svih 65536 stanja proširenog kodera. Dodatno su proverena svih osam stanja DMUX-a, četiri vrednosti F i **1048576 slučajeva** stabla MUX 16/1 (svaka adresa i svaka 16-bitna reč). [Logički dokaz](logicka_provera_s011_s015.json) dopunjuje pregled topologije. Završni logovi oba PDF-a nemaju upozorenja, prekoračenja prostora, greške, nerešene reference ili nedostajuće znakove.

[Notes log](../../build/redizajn/dorada-s011-s015-2026-10-09/notes.log), [review log](../../build/redizajn/dorada-s011-s015-2026-10-09/review.log), [check log](../../build/redizajn/dorada-s011-s015-2026-10-09/check.log).

## Isporuka i poređenje

- [Prezentacija — 22 slajda](../../build/03_kola_srednjeg_stepena_integracije.pdf)
- [PDF beležaka — 22 A4 strane](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf)
- [Uporedni pregled](../../build/redizajn/pregled/index.html#03-s011)
- [Neposredno prethodni pregled](../../build/redizajn/pre-dorade-s011-s015-2026-10-09/pregled/index.html)
- [Prethodni izveštaj s004/s007–s010](istorija/pre-dorade-s011-s015-2026-10-09/izvestaj.md)
- [Sačuvani prethodni izvori](istorija/pre-dorade-s011-s015-2026-10-09/izvori/)

| Primer | Pre | Posle |
|---|---|---|
| DMUX s012 | [Prethodna šema](../../build/redizajn/pre-dorade-s011-s015-2026-10-09/pregled/novi/p-13.png) | [Potpuna realizacija](../../build/redizajn/pregled/novi/p-13.png) |
| Strelice s014 | [Prethodni raspored](../../build/redizajn/pre-dorade-s011-s015-2026-10-09/pregled/novi/p-15.png) | [Povezane formula i realizacija](../../build/redizajn/pregled/novi/p-15.png) |
| Stablo s015 | [Prethodni raspored](../../build/redizajn/pre-dorade-s011-s015-2026-10-09/pregled/novi/p-16.png) | [Razdvojene celine](../../build/redizajn/pregled/novi/p-16.png) |

Izlazi u `build/` ne verzionišu se; navedene komande obnavljaju ih iz izvora. Originalni PDF, istorijska mapa, zajednička tema i ostala predavanja ostaju neizmenjeni.

## Otisci pregledane verzije

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Izvorna mapa | `a3effdb79779d04df05ce98ece642a6068684e4b798018cc96122479136266cc` |
| Manifest redizajna | `72850e06c0f56c19b48e63cecbeafc78c51b42541927ec56d951ceae9ba513ea` |
| Zapis izgradnje | `049201c84755677bec4c0afe9e15a5aab6cf0e0d07b9f840fedf360942102804` |
| Potvrde pregleda | `5307844c4db788fc939d88a6af6bef19296af21ca99af5d7b60a753d9b0912b8` |
| Pokrivenost | `1d2d8ac7d63412fef3f5d4c16d276995a78da583924114432d5988838e3c6a8a` |
| Evidencija beležaka | `8c5d09daa6bc10bf002246eb0f6f102bde6b96c0bebf5d6f93c2f3b1cffc189c` |
| Prezentacioni PDF | `c85832ed0786e227fa303cac68311c5c9e8ec80c99ffc6a8a8b7e6293aa6af63` |
| PDF beležaka | `e11c0864236b5c49aaf75285e8fdcbc551bc867caf9bacbe686207ea0b86b0b0` |
| Dokaz nepromenjenih prikaza | `fbd2e67189cfdba1d49ce79ce5fb9a5ca55e4c60540beb8d5fa70c103b1b6924` |
| Logički dokaz | `d84e4c8b6f6762f4d9ad5b2de262021ab13a142bc6c604c3188dcdb8d8d98c21` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak

Tražena dorada s011–s015 je završena. Sledeća radnja je korisnikov pregled ove verzije 03, status `ceka_odobrenje`. Cela prezentacija 03 još nije prihvaćena. Ranija dorada s004/s007–s010 i odobreni s010b ostaju očuvani; njihova istorija je u prethodnom izveštaju i odlukama. Novi agent proverava relevantne otiske i nastavlja po korisnikovom nalogu bez ponavljanja završene analize nepromenjenih izvora.
