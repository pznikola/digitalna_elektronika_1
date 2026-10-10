# Računski dokazi predloga — 09_1

Dokazi potiču iz modela originala. Oni su tehnička evidencija, nisu nastavni dodatak niti primenjena ispravka. Nove formule u slajdovima čekaju korisnikovu odluku prema planu.

## P08 i P12: ponovno izvođenje

Pišemo `ρ=k_L/k_D`, `A=V_C−V_TL`, `B=V_C−V_DD−V_TL`. Ravnoteža dva omska modela:

```text
ρ[(A−V_O)²−B²] = V_O(2V_I−2V_TD−V_O).
```

Za zasićeno opterećenje isto važi uz `A=V_DD−V_TL`, `B=0`. Diferenciranje uz `V_O'=-1` daje:

```text
2ρ(A−V_O) = −(2V_I−2V_TD−V_O) + 3V_O
           = 4V_O−2V_I+2V_TD.
V_I = V_TD+(2+ρ)V_O−ρA.
```

Zamenom ulaza u desnu stranu ravnoteže:

```text
ρ(A²−2AV_O+V_O²−B²)
  = V_O[(3+2ρ)V_O−2ρA].
ρ(A²−B²) = (3+ρ)V_O².
```

Uz nenegativan izlaz bira se pozitivni koren. Rezultat zatim treba proveriti prema uslovima modela, a ne samo prema jednačini. Za ilustrativne parametre `V_DD=5`, `V_TD=V_TL=0,7`, `k_L=0,2`, `k_D=1`:

| Opterećenje | Parametri | Novi VO(IH) | Novi VIH | Provera režima |
|---|---|---:|---:|---|
| Omsko, VC=7 | A=6,3, B=1,3 | 1,541104 | 2,830429 | TD omski: VO<VI−VT; TL omski: VDD−VO<VC−VO−VT |
| Zasićeno, VC=VDD | A=4,3, B=0 | 1,075000 | 2,205000 | TD omski: VO<VI−VT; TL zasićen jer VDS=VGS |

Oba nova para daju jednake struje i nagib −1. Izvorni parovi daju različite struje, što već proverava `kodovi/provera_logike.py`. Brojevi su isključivo protivprimer/dokaz, ne novi primeri koji su pripisani originalu.

## Ostali predlozi

- P02: u granični uslov `VO=VI−VT` unosi se ravnoteža `(VDD−VO)/RL=kn(VI−VT)²/2`; nastaje `knRL x²/2+x−VDD=0`. Pozitivni koren daje predlog.
- P03: za odnos 0,5 stvarni faktor imenitelja je 2/3. Sama nejednakost `<1` ne dopušta zamenu faktora sa 1.
- P04: na primer, granica zasićenja 0,2 V i srednji nivo 2,5 V ispunjavaju proveru pri kašnjenju, ali izlaz 0,1 V više ne ispunjava uslov zasićenja. To je dokaz logičkog opsega zaključka, ne zadat model iz prezentacije.
- P05: decimalni razvoj razlomaka nije konačan; `7/9=0,777…` zaokružuje se na 0,778.
- P07: pri jednakim k u kvadratnoj jednačini nestaju oba člana sa razlikom k; preostaje `−Δ²k_L=0`.
- P09: neposredno razvijanje definicije Δ daje dodatni faktor 2 uz VT,L.
- P10: `k_D[(k_L/k_D)(A−VO)]²=(k_L²/k_D)(A−VO)²`.
- P11: u izrazu za nagib odnos jednak jedan daje −1, dok odnos veći od jedan daje nagib sa apsolutnom vrednošću većom od jedan.
- P13: zameniti VOH u već prikazani imenilac, bez novog modela.

Datum provere: 2026-10-03. Dodatna provera oba nova para, ravnoteže i izvoda sačuvana je u `dokazi_ispravki.json`. Ona ne menja istorijski skup od 231 računskog poređenja.
