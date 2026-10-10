# Otvorena stručna pitanja — 06

Status: odluka nije primljena. Originalni sporni zapisi ostaju na slajdovima; ovaj nalog ne odobrava stručne ispravke.

| Grupa | Slajd | Predlog i dokaz |
|---|---|---|
| 1 | s007 | Prvi operand 53 promeniti u 43, da se slaže sa svim narednim redovima. Umesto obične jednakosti 76₁₀ = −24₁₀ napisati „Kod 76 u dvocifrenom desetkovom komplementu predstavlja −24“, uz ograničenje da je ovde reč o negativnom rezultatu. 19−43=−24; 100−24=76. |
| 2 | s013 | Dopuniti frakciju prve kodne reči završnom nulom do 23 bita: 0 10000010 10101000000000000000000. U drugom primeru −101001₂ zameniti sa −10100100₂. 1.01001₂·2⁷=164; 101001₂=41. Provereno pomoću Python struct binary32. |
| 3 | s014 | Normalne eksponente obuhvatiti uslovom 1≤E≤254. E=1,F=0 daje 2⁻¹²⁶, a E=254,F=0 daje 2¹²⁷: oba su konačna normalna broja. |
| 4 | s016 | Težine osam one-hot položaja navesti kao 0,1,2,…,7. Tabela već postavlja jedinicu u najdesniji položaj za vrednost 0. |
| 5 | s021 | Povratne formule od trećeg reda naniže zameniti kumulativnim XOR-om: bᵢ=bᵢ₊₁⊕gᵢ, odnosno bᵢ=gₙ₋₁⊕…⊕gᵢ. G=1100 vraća B=1000; susedni XOR iz originala daje 1010. |
| 6 | s028/s029 | Ukloniti x na poziciji 13 u redu r₁/p₁ u obe tabele. 13=1101₂ ima drugi bit od desne strane 0. Pogrešan dodatni x daje sindrom 1111 za grešku na poziciji 13 umesto 1101. |
| 7 | s019 | „Greška očitavanja vrednost bita najniže težine“ zameniti sa „Očitana vrednost može odstupati za jedan korak“. Menja se D₃, pa tvrdnja o najnižem bitu nije doslovno tačna; Grejov kod nije težinski. U prikazanom prelazu prijemnik čita 8 ili 7. |
| 8 | s029 | Uz oba zaključka o sindromu dodati „Ako je nastala najviše jedna greška“. Nula sindroma ne isključuje višebitnu grešku: promene na pozicijama 1,2,3 daju 1⊕2⊕3=0. Kod d=3 ispravlja jednu grešku; pri dve greške automatsko ispravljanje može promeniti treći bit. |

Dodatna objašnjenja u beleškama ne služe za prećutno razrešenje ovih pitanja. Posle korisnikove odluke primeniti odobrene grupe, pregledati pogođene slajdove i beleške i obnoviti potvrde. Prihvatanje cele prezentacije i početak 07 vode se zasebno.

Predlozi za pokretni zarez i dopune provereni prema [Oracle — Single Format](https://docs.oracle.com/cd/E37069_01/html/E39019/z4000ac019178.html), pregledano 2026-10-02. Izvor navodi polja 1/8/23, normalne eksponente 0<E<255 i subnormalnu vrednost sa faktorom 2⁻¹²⁶.
