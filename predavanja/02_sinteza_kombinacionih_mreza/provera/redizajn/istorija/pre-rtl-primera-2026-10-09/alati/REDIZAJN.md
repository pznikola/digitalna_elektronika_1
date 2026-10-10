# Alati za redizajn i beleške

Ovi alati sprovode tehnički deo [plana](../../PLAN_PREDAVANJA.md). Izbor B je usvojen. Nastavna predavanja nisu pokrenuta pripremom infrastrukture; početak i prelazak na sledeće predavanje prate [centralnu evidenciju](../../STATUS_PREDAVANJA.md).

## Komande i režimi

Iz korena repozitorijuma, uz **obavezan izbor jednog predavanja**:

```bash
make -C predavanja LECTURE=01_logicke_funkcije all
make -C predavanja LECTURE=01_logicke_funkcije notes
make -C predavanja LECTURE=01_logicke_funkcije review
make -C predavanja LECTURE=01_logicke_funkcije check
```

Ovo su primeri sintakse, ne nalog da se 01 pokrene pre odobrenja. Bez `provera/redizajn/manifest.json` alati zadržavaju provere rekonstrukcije; `notes` tada odbija rad uz objašnjenje. Manifest mora imati `phase: redizajn`; nepoznata faza je greška, bez prećutnog vraćanja na istorijske potvrde.

U redizajnu `all` gradi samo projekcioni PDF, `notes` gradi prezentaciju i A4 beleške, `review` gradi oba PDF-a i uporedni HTML, a `check` uz to proverava pokrivenost, nove potvrde i postojeću računsku proveru. `review` može prikazati nedovršen sadržinski rad; `check` ga odbija. Nijedna komanda automatski ne daje sadržinsku potvrdu ili korisnikovo odobrenje.

`preview` nije dostupan u redizajnu jer svi postojeći slajdovi moraju ostati prisutni. `clean` odbija brisanje foldera koji čuva početni prikaz. `inventory` pripada istorijskoj rekonstrukciji, ne novoj sadržinskoj analizi. Izgradnja je lokalna, LuaLaTeX/latexmk sa `-no-shell-escape`.

## Početak samo odobrenog predavanja

1. Pročitaj centralno stanje, odluke i izveštaj. Ako evidencija redizajna već postoji, nastavi od nje, bez ponovnog `init`.
2. Sačuvaj stvarnu korisnikovu poruku koja odobrava početak u UTF-8 tekstualni fajl. To nije nova potvrda koju alat traži od korisnika: koristi već dato, važeće odobrenje. Agent je odgovoran za proveru obima odluke i redosleda predavanja; alat ne tumači prirodni jezik odobrenja.
3. Pokreni, sa stvarnom putanjom fajla odluke:

   ```bash
   python3 predavanja/_alati/redizajn.py init \
     --lecture 01_logicke_funkcije --theme etf-v1 \
     --decision-file /putanja/do/stvarne-odluke.txt
   ```

4. `init` kompajlira trenutno predavanje pre promena i čuva PDF, redosled ID-jeva, PNG prikaze, kopije lokalnih izvora, korišćene resurse i kontrolne sume zavisnosti u `build/redizajn/pre/`. Paketi i fontovi sistema imaju otiske i verzije alata; za obnovu početnog prikaza potrebno je odgovarajuće TeX okruženje. Snapshot i njegov potpis ostaju nepromenjeni. Napravi trajnu rezervnu kopiju `pre/` izvan ignorisanog `build/` pre čišćenja ili prenosa rada.
5. Nastaju prazna evidencija i izvori beležaka, sa statusima `ceka` i nepotvrđenim inventarom. Glavni izvor prezentacije **ne prebacuje se automatski** na novu temu. U okviru odobrenog redizajna primeni [uputstvo etf-v1](../_zajednicko/etf-v1/README.md), pa analiziraj original i postojeće slajdove po planu.
6. Ručno ažuriraj centralni status na `u_radu`, sa odlukom, manifestom, njegovim SHA-256 i narednim korakom. `init` ne prepisuje centralnu evidenciju niti odobrava druga predavanja.

`init` odbija prepisivanje postojećeg redizajna, početnog prikaza ili beležaka. Posle tehnički prekinute inicijalizacije proveri sačuvane artefakte pre oporavka; ne briši jedinu početnu kopiju da bi ponovo pokrenuo komandu.

## Fajlovi i odgovornosti

| Fajl | Sadržaj i održavanje |
|---|---|
| `provera/mapa.json` | Postojeći stabilni ID-jevi, broj, redosled i položaji originalnih slajdova |
| `provera/redizajn/manifest.json` | Faza, predavanje, B, konkretna tema i SHA njenog manifesta, original, početni snapshot, niz ID-jeva, putanje i naslovi beležaka |
| `provera/redizajn/inventar.json` | Nezavisan, ručno potvrđen sadržajni popis originala i postojećih dopuna |
| `provera/redizajn/pokrivenost.json` | Proverljiva odredišta elemenata na slajdu i u beleškama istog ID-ja |
| `provera/redizajn/pokrivenost.md` | Čitljiva tabela generisana iz prethodna dva JSON-a; menjati izvore, ne ovu tabelu |
| `provera/redizajn/pregled.json` | Nove potvrde posle stvarnog pregleda, datum, izvršilac, opis i dokazi |
| `provera/redizajn/izgradnja.json` | Automatski zapis aktuelnih ulaza, izlaza, komandi i verzija alata; **nije potvrda pregleda** |
| `provera/redizajn/odluke.md`, `izvestaj.md` | Stvarne odluke i tekući/završni izveštaj po planu |
| `beleske/sNNN.tex` | Jedini uređivi izvor detaljnih beležaka tog slajda |
| `<folder>_beleske.tex` | Generisani dokument za čitanje; obnavlja se pri `notes`, ne uređivati ručno |
| `build/redizajn/pregled/otisci.json` | Dokazi trenutnih prikaza i izvora po ID-ju; prenose se u potvrdu tek posle pregleda |

Manifest upućuje na `izgradnja.json`, koji sadrži detaljne otiske stvarno korišćenih zavisnosti i oba PDF-a. Pri predaji evidentiraj otiske **oba** fajla u izveštaju i centralnoj evidenciji. Automatsko obnavljanje izgradnje ne menja `pregled.json`.

## Beleške

Za svaki slajd postoji tačno jedan `beleske/sNNN.tex`. Početak je obavezno, na primer:

```latex
\BeleskeID{01-s003}
\section*{Objašnjenje iz originala}
% element: 01-s003:e02
Detaljno obrazloženje preneto sa istog slajda.

\section*{Dopunsko objašnjenje}
Provereni međukoraci i tumačenje oznaka, jasno odvojeni od originala.
```

Kratkom/naslovnom slajdu nije potreban veštački dugačak tekst; vezu sa ID-jem ipak mora imati. Naslov u `manifest.notes.<ID>.title` je običan tekst; formule piši u samim beleškama. Beleške podržavaju standardni LaTeX za tekst, formule, tabele i kod. Posebne lokalne naredbe moraju se definisati/uključiti u izvoru beležaka; Beamer overlay naredbe nisu dozvoljene.

A4 dokument prikazuje tačnu stranu upravo izgrađene prezentacije, ID, naslov i beleške. Svaki blok počinje novom stranom; duge beleške nastavljaju se sa istim ID-jem u zaglavlju. `.notes-map.tsv` beleži stvarno poslate strane: svaki ID mora imati jedan neprekinuti blok, istim redosledom kao slajdovi. `.slide-map.tsv` zasebno mora ostati tačno jedan ID po prezentacionoj strani.

## Pokrivenost sadržaja

Popis ne nastaje samo iz tekstualnog izvlačenja. Pregledaj svaki original i postojeći prikaz, uključujući slike, formule, tabele i šeme. `inventar.json` ima ovu strukturu, sa više elemenata po slajdu:

```json
{
  "slides": {
    "01-s003": {
      "confirmed": true,
      "elements": [
        {
          "id": "01-s003:e02",
          "description": "Detaljno obrazloženje postupka",
          "source": "PDF strana 2, gornji slajd, pasus ispod formule",
          "origin": "original",
          "must_remain_visible": false
        }
      ]
    }
  }
}
```

`confirmed: true` unosi se **posle** potpunog sadržinskog popisa; primer nije gotov inventar predavanja. `origin` je `original`, `postojeca_dopuna` ili `dopuna`. Definicije, rezultati, uslovi, nastavne šeme/tabele i drugi ključni elementi moraju imati `must_remain_visible: true`.

Odgovarajući unos u `pokrivenost.json`:

```json
{
  "slides": {
    "01-s003": [
      {
        "element": "01-s003:e02",
        "slide": null,
        "notes": {
          "path": "beleske/s003.tex",
          "anchor": "% element: 01-s003:e02"
        },
        "change": "Detaljno obrazloženje preneto u beleške istog slajda",
        "status": "provereno"
      }
    ]
  }
}
```

`slide` koristi isti oblik odredišta (`path`, `anchor`). Element može biti raspoređen na oba mesta. Putanja mora biti sam slajd/beleška ili njihov uključeni lokalni izvor; tekst sidra mora stvarno postojati u njemu. Za vidljiv sadržaj odredište na slajdu je obavezno. Svaki element inventara mora imati tačno jedan red pokrivenosti i bar jedno odredište, bez nepoznatih/dupliranih elemenata.

Sidro proverava lokaciju, **ne značenje**: agent mora pregledati sve pripadajuće prikaze i potvrditi da sadržaj na lokaciji odgovara originalu. Ne proglašavati celu logičku celinu sporednim obrazloženjem radi premeštanja u beleške.

## Potvrde, zavisnosti i nastavak

Posle pregleda sva četiri prikaza za jedan ID, u njegov unos `pregled.json` upiši:

- `categories`: `tekst`, `formule`, `tabele`, `kod`, `crtezi`, `citljivost`, `pokrivenost`, `beleske`;
- status kategorije `provereno` ili obrazloženo `nije_primenljivo`; obavezne kategorije i sadržaj prisutan u inventaru ne mogu biti neprimenljivi;
- `date`, `reviewer`, `notes`: stvarni datum, izvršilac i konkretan opis pregleda;
- `evidence`: ceo objekat baš tog ID-ja iz aktuelnog `build/redizajn/pregled/otisci.json`.

Dok pregled nije izvršen koristi `ceka` ili `problem`. Nema komande za automatsko potvrđivanje. `check` proverava pokrivenost i važenje svih dokaza, pa odbija staru potvrdu čak i kada se promenio samo komentar u izvoru beležaka, a prikaz ostao isti.

U režimu redizajna zavisnosti dolaze iz stvarnih LaTeX `.fls` ulaza, uz manifest, mapu, alate i računsku proveru. Fontovi i paketi su uključeni. Izabrana tema je vezana svojim manifestom; druga, nekorišćena tema nema uticaj. Stari režim rekonstrukcije zadržava svoj `dependency_digest` i svoje istorijske potvrde.

Potvrde po slajdu imaju zasebne otiske njegovih izvora, beležaka, svih pripadajućih prikaza i pokrivenosti. Izmena jednog izvora beležaka poništava pogođenu potvrdu. Zajednički izvori/tema i dinamičke zavisnosti čiji obim ne može pouzdano da se razdvoji traže pregled svih pogođenih slajdova. Promena broja strana ranijih beležaka može promeniti numeraciju i prikaz kasnijih; proveri sve zaista izmenjene prikaze.

Ako se promeni korišćena tema, provera odbija nepodudaranje sa pinovanim manifestom. Dok nijedno predavanje na njoj nije odobreno, doradu evidentiraj, proveri i potom izmeni vezu u manifestu; sve pogođene potvrde postaju zastarele. Posle odobrenja koristi novu verziju teme prema planu. Ne osvežavaj otiske da bi prikrio promenu.

HTML i PDF izlazi ostaju u `build/`. Izvori, evidencija i potvrde ostaju izvan njega. Ako izlazi nedostaju, obnovi izgradnju i pregled; potvrde važe samo ako se dokazi poklapaju. Nedostajući početni snapshot vraća se iz rezervne kopije, nikad iz redizajniranog PDF-a.

## Provere infrastrukture

```bash
make -C predavanja test
make -C predavanja test-redizajn
```

Prva komanda obuhvata postojeće i nove regresione testove. Druga pravi izolovan primer u `_alati/build/proba_redizajna/`, sa dva izmišljena slajda i tri strane beležaka; ne analizira nastavna predavanja. Test proverava i javne funkcije `all/review/check`, odbijanje nepotvrđenog sadržaja, promenu samo beležaka, pogrešan ID, korišćenu/nekorišćenu temu, početni prikaz i očuvanje istorijske evidencije. Test potvrde su jasno označeni podaci testa i ne predstavljaju pregled nastavnog gradiva.

Uspešna automatska provera ne dokazuje ispravnost topologije kola, stručnog sadržaja ili čitljivost svih oznaka. Potreban je stvarni pregled svakog slajda i svih beležaka, pa izveštaj i korisnikova odluka po planu.

## Izričito odobrena podela originalnog slajda

Podrazumevani režim i dalje zahteva jedan originalni slajd, jedan okvir i jednu prezentacionu stranu. Korisnik je 2026-10-03 izričito tražio da se s002 i s009 predavanja 02 podele na po dva slajda. Za taj evidentirani izuzetak manifest sadrži `approved_splits`: putanju i SHA-256 odluke, te uređeno mapiranje izvornih ID-jeva na izvore nastavaka. Odluka čuva stvarni korisnikov tekst, predavanje, `action: split_into_two` i tačan niz `source_ids`. Agent ne stvara odobrenje bez stvarnog naloga.

Istorijska `provera/mapa.json` i katalog ostaju neizmenjeni. Iz njih alat izračunava izlazni niz: prvi deo zadržava ID i putanju; nastavak dobija sufiks `b`, izvor `slajdovi/sNNNb_nastavak.tex` i zasebne beleške `beleske/sNNNb.tex`. Na primer, `02-s002 → 02-s002b → 02-s003`. Manifest mora sadržati upravo taj niz i isto uređene beleške. Proveravaju se svi originali, broj izlaznih strana, redosled, duplikati, tačno jedan okvir po izvoru i ID-jevi oba PDF-a. Izostavljeno ili promenjeno odobrenje, druga izvorna celina ili pogrešno vezane beleške ne prolaze. Overlay-i i automatsko smanjivanje ostaju zabranjeni.

Original i početni prikaz u uporednom pregledu vezuju se za izvorni broj, dok se novi slajd i A4 blok vezuju za izlaznu stranu. Oba dela zato prikazuju isti odgovarajući original i početni slajd. Svaki deo ima sopstveni sadržajni inventar, pokrivenost i potvrdu; tehnička mapa podele povezuje ranije elemente sa njihovim novim odredištima. Izmenjeni izvori ili alati poništavaju pogođene potvrde kao i u redovnom režimu. Ovo ne odobrava druge podele.

Vidljivi urednički naslovi u starom primeru beležaka iznad nisu obavezni: sadržinska pravila aktuelnog `PLAN_PREDAVANJA.md` imaju prednost. Beleške sadrže samo dodatno nastavno objašnjenje za predavača.
