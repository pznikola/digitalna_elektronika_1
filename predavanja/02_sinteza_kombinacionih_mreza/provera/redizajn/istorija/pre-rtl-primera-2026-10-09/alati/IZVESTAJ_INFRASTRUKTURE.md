# Izveštaj — infrastruktura redizajna i beležaka

Datum: **2026-09-25**. Obim naloga „odradi sledeci korak“: prethodno najavljena podrška za beleške, pokrivenost i potvrde redizajna. Rad na nastavnom predavanju 01 nije započet. Stil B i kompaktne analogne šeme ostaju usvojeni.

## Implementirano

- Eksplicitan režim `phase: redizajn`, uz očuvan režim rekonstrukcije i njegove potvrde. Broj, redosled, izvorne lokacije i stabilni ID-jevi proveravaju se prema katalogu, mapi i stvarno poslatim PDF stranama.
- `init` za samo jedno odobreno predavanje: početni PDF, PNG prikazi, kopije lokalnih izvora i resursa, zavisnosti i otisci. Inicijalizacija ne menja temu glavnog izvora i ne potvrđuje sadržaj.
- `notes`: izgradnja projekcionog PDF-a i zasebnog A4 dokumenta iz po jednog LaTeX izvora beležaka za svaki slajd. Beleške mogu imati više strana uz isti ID u zaglavlju; prezentacija ne dobija dodatne strane.
- Nezavisan sadržajni inventar, uređiva mapa pokrivenosti slajd/beleške i generisana Markdown tabela. Ključni sadržaj mora imati vidljivo odredište na slajdu. Proveravaju se i veze sa stvarnim lokalnim izvorima i sidrima.
- HTML pregled originala, prethodnog prikaza, novog slajda i svih strana njegovih beležaka. Nedostajući početni prikaz se odbija.
- Nove potvrde po slajdu vezane za sadržajni popis, izvore, korišćenu temu i prikaze slajda/beležaka. Promena beležaka poništava pogođenu potvrdu čak i bez vizuelne promene.
- Stvarne `.fls` zavisnosti, fontovi i verzije alata; dodatak nekorišćene teme ne menja važeći pregled. Evidencija izgradnje odvojena je od ručnih potvrda.
- Obavezan `LECTURE` za komande nad predavanjem i zaštita početnog snapshot-a od `clean`.

Detaljna upotreba, šeme JSON-a, primeri beležaka i postupak nastavka: [REDIZAJN.md](REDIZAJN.md).

## Rezultati provera

| Provera | Rezultat |
|---|---|
| `make -C predavanja test` | 36 testova prolazi, uključujući prethodnih 20 |
| `make -C predavanja test-redizajn` | Prolazi kompletna proba na izmišljenom materijalu |
| Broj i mapiranje u probi | Dva slajda, dve prezentacione strane, tri strane beležaka; ID sa donjom crtom i višestranični nastavak |
| Nepotvrđen sadržaj | Odbijen dok postoje test statusi `ceka` |
| Pokrivenost | Odbijeni izostavljen/dupliran element, nepostojeće odredište, tuđe beleške i ključni sadržaj sakriven u beleškama |
| Izmena samo beleške prvog slajda | Zastarela potvrda prvog; potvrda nepogođenog drugog ostaje važeća |
| Pogrešan ID / nedostajući resurs / početni PDF | Odbijeni |
| Korišćena / nekorišćena tema | Promena korišćene odbijena; druga nekorišćena tema ne poništava pregled |
| Istorijske potvrde | Sačuvane, ne koriste se kao potvrde redizajna |
| Komande bez `LECTURE` | Svih šest ciljeva odbijeno pre rada nad predavanjima |
| Galerija i izdvojena tema | Obe provere prolaze; svih deset postojećih prikaza teme ostalo pikselno identično |
| Nastavni materijal | Originalni PDF-ovi, LaTeX slajdovi, stari stilovi i istorijske potvrde neizmenjeni |

U odnosu na 1.465 ranije evidentiranih fajlova promenjeno je samo pet planiranih infrastrukturnih/dokumentacionih fajlova: `predavanja/Makefile`, `predavanja/README.md` i tri ulazna Python alata (`izgradnja.py`, `provera.py`, `uporedni_pregled.py`). Novi izvori infrastrukture su dodati odvojeno. Nijedno od 12 nastavnih predavanja nema inicijalizovan manifest redizajna.

Vizuelno pregledane sve tri strane demonstracionih beležaka: ispravni slajdovi, ID-jevi, nastavak, formule i fontovi, bez odsecanja i preklapanja. Test namerno ima kratak tekst i zasebnu stranu nastavka radi provere mapiranja; nije predlog da beleške nastavnih slajdova budu veštački razvučene. Logovi ne sadrže prelivanja, nedostajuće znakove, zamene fontova ili nerešene reference. Lokalni linkovi uporednog pregleda su provereni.

## Tehnička dorada teme

Proba ID-ja sa donjom crtom otkrila je da podnožje `etf-v1` tretira `_` kao matematički znak. Ispravljen je samo bezbedan tekstualni ispis ID-ja. Sadržaj ID-ja u TSV zapisu, fontovi, geometrija i svih deset ranijih prikaza ostali su isti. Proba sa `DEMO_1-s001` sada prolazi.

Aktuelni manifest teme: `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`. Prethodni manifest i PNG prikazi sačuvani su u `../_zajednicko/etf-v1/build/pre-podrska-id/`. To je evidentirana dorada pre prvog odobrenog nastavnog predavanja; [pravilo zamrzavanja teme](../_zajednicko/etf-v1/README.md) ostaje na snazi. Pri izradi beležaka ispravljen je i redosled zatvaranja zapisa strana, da obuhvati poslednju A4 stranu.

## Demonstracioni izlazi

- [Prezentacija](build/proba_redizajna/demo/build/demo.pdf)
- [PDF beležaka](build/proba_redizajna/demo/build/demo_beleske.pdf)
- [Uporedni pregled](build/proba_redizajna/demo/build/redizajn/pregled/index.html)
- [Rezultat integracione probe](build/proba_redizajna/rezultat.json)

Izlazi su u ignorisanom `build/`; obnavljaju se komandom `make -C predavanja test-redizajn`. Sadržinske potvrde u tom folderu eksplicitno su označene kao test podaci. Alati za nastavna predavanja nikad ne popunjavaju potvrde automatski.

## Granice i naredni korak

Automatska provera potvrđuje strukturu i aktuelnost evidencije, ali ne može sama dokazati kompletnost ručnog inventara, stručnu vernost ili čitljivost svake šeme. Agent mora stvarno pregledati original, slajd i beleške, pa popuniti potvrde. Sistemski paketi/fontovi beleže se otiscima; za reprodukciju snapshot-a potrebno je sačuvati odgovarajuće okruženje i njegovu lokalnu rezervnu kopiju.

Spremno je sve za odobreni početak **predavanja 01**. Posle korisnikovog naloga inicijalizovati samo 01, analizirati i redizajnirati njegovih 37 slajdova, napisati beleške, izvršiti provere i predati izveštaj. Predavanje 02 ostaje nezapočeto do zasebnog odobrenja prelaska. Merodavna je [centralna evidencija](../../STATUS_PREDAVANJA.md).
