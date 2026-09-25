# Uočene greške i nedoumice u originalu

Sve navedeno preneto je verno. Predlozi nisu primenjeni u prezentaciji.
Lokacija: broj slajda; originalna PDF strana je ceil(slajd/2), neparni je gore.

| Slajd | Originalni zapis | Nalaz i predlog |
|---|---|---|
| 2 | „informacije su takođe predstavljen“, „u drugom komplenetu“ | Slovne greške; predlog „predstavljene“, „komplementu“. |
| 5 | „kao prikazati“ | Verovatno „kako prikazati“. |
| 7 | Prvi red 19−53, nastavak 19−43 | Nastavak i rezultat −24 odgovaraju 19−43; 19−53 je −34. |
| 7 | 76₁₀ = −24₁₀ | Kao obična decimalna jednakost nije tačno. 76 predstavlja −24 samo uz izričit dogovor o dvocifrenom komplementnom kodu. Predlog razlikovati kodnu reč i vrednost. |
| 8 | „sa levo“ | Predlog „sa leve strane“. |
| 13 | Prvi „Zapis“: 0 10000010 1010100000000000000000 | Prikazano je 22 umesto 23 bita frakcije; nedostaje završna nula. Pravi binary32 zapis za 13.25 nezavisno proveren pomoću struct. |
| 13 | −101001₂ = −164₁₀ | Binarna vrednost je −41. Za −164 treba −10100100₂; raniji eksponent 7 i mantisa odgovaraju −164. |
| 14 | 1 < E < 254 za normalizovane vrednosti | Granice treba uključiti: 1 ≤ E ≤ 254. Obe rubne vrednosti daju konačne normalizovane binary32 brojeve. |
| 16 | „one hot“ … „biti težine 1,2,3,4…6,7“ | Tabela ima osam položaja i predstavlja vrednosti 0–7. Za tu tabelu težine položaja počinju od 0; tekst izostavlja početnu nulu. |
| 21 | b(n−3)=g(n−2)⊕g(n−3), …, b₀=g₁⊕g₀ | Povratna konverzija zahteva kumulativni XOR svih viših Grejovih bitova. Rekurzivno bᵢ=b(i+1)⊕gᵢ. Prva dva prikazana reda jesu ispravna; ostali uopšteno nisu. Nezavisan kontraprimer: G=1100 odgovara B=1000, a susedni XOR daje 1010. |
| 26 | „raastojanje“, „Hemnigovo“ | Predlog „rastojanje“, „Hemingovo“. |

| 28–29 | Dodatni x na poziciji 13 u redu r₁/p₁ | 13=1101₂ nema jedinicu na bitu 1. Taj x ne pripada ovom redu standardne Hemingove matrice; treba ga ukloniti u ispravljenom izdanju. Ovde je sačuvan u obe tabele. |

Zapis `F<>0`, odvojeni znakovi `>=`, nestandardna interpunkcija i prazne ćelije sačuvani su bez prećutnog usklađivanja. Slajd 25 namerno prikazuje alternativne bite pri prijemu u zagradama; to nisu greške.
