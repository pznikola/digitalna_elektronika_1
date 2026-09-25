# Inventar — vežba 02

Prethodni sadržaj sačuvan: 4 rešena zadatka, 2 zadatka za samostalni rad na kraju i svi dodatni zahtevi u okvirima. Rešenja ranije nerešenih zahteva nisu dopisana u studentski dokument. Neusklađeno rešenje 3d objašnjeno je uz očuvanje postavke i originalne šeme.

| Celina | Sadržaj i dokaz provere |
|---|---|
| 1a/b | MUX4/1, četiri reda funkcionalne tabele, tri formule, dve šeme, dva VHDL primera. Domeni: 64 i 16 kombinacija. |
| 2a–d | Šenonovi kofaktori; četiri NI2 kola; broj kućišta i kašnjenje; sve tri Karnoove karte, obe strelice, hazard i dodatni CA. Tri VHDL primera; oba modela kašnjenja; nerešeni zahtev selekcije AC sačuvan. |
| 3a–d | Tabela i osam minterma dekodera; aktivni niski nivoi i sve dozvole; 4/16; funkcija preko izlaza 0,2,7; Karnoova karta; 6/64 i uslovljena alternativa. Tri VHDL primera plus dva pomoćna dekodera. |
| 4a–c | Dve 16-redne tabele BCD; 14 Karnoovih karata; sve transformacije sedam segmenata; NOT/NILI konvencija; upravljačka tabela; ERROR, OFF, LZ; višecifrena kaskada, protokol i ograničenja povratne sprege. Svi dodatni zahtevi sačuvani. |
| Samostalni 1a–c | Sastavljanje dekodera; 4/16 iz I2/NE; mogućnost 13-ulaznog dekodera u četiri nivoa proverena iscrpno. Bez novih rešenja u PDF-u. |
| Samostalni 2a–d | Sva četiri para selekcije i sva stanja; privatna provera minimuma uz izričito navedenu biblioteku. U tekstu naveden nedostajući uslov poređenja. |

Ukupno: 6 tabela (uključujući opis upravljačkih signala), 18 Karnoovih karata, 22 numerisane slike (od toga 16 uključenih ilustracija i 14 podslika unutar dve zbirne slike), 8 uključenih VHDL listinga. Pored listinga pregledani su svi pomoćni moduli i testbenčevi.

## Uključene ilustracije

| Izmenjivi izvor | Izvoz |
|---|---|
| `Images/Zadatak_1/Zadatak_1b.drawio` | `Images/Zadatak_1/Zadatak_1b.pdf` |
| `Images/Zadatak_1/Zadatak_1a.drawio` | `Images/Zadatak_1/Zadatak_1a.pdf` |
| `Images/Zadatak_2/Zadatak_2a.drawio` | `Images/Zadatak_2/Zadatak_2a.pdf` |
| `Images/Zadatak_2/Zadatak_2b.tex` | `Images/Zadatak_2/Zadatak_2b.pdf` |
| `Images/Zadatak_3/Zadatak_3a.drawio` | `Images/Zadatak_3/Zadatak_3a.pdf` |
| `Images/Zadatak_3/Zadatak_3b.drawio` | `Images/Zadatak_3/Zadatak_3b.pdf` |
| `Images/Zadatak_3/Zadatak_3c.drawio` | `Images/Zadatak_3/Zadatak_3c.pdf` |
| `Images/Zadatak_4/7seg.drawio` | `Images/Zadatak_4/7seg.pdf` |
| `Images/Zadatak_4/Zadatak4_a.drawio` | `Images/Zadatak_4/Zadatak4_a.pdf` |
| `Images/Zadatak_4/Zadatak_4b.drawio` | `Images/Zadatak_4/Zadatak_4b.pdf` |
| `Images/Zadatak_4/Zadatak_4c_OffInternal.drawio` | `Images/Zadatak_4/Zadatak_4c_OffInternal.pdf` |
| `Images/Zadatak_4/Zadatak_4c_Lzout.drawio` | `Images/Zadatak_4/Zadatak_4c_Lzout.pdf` |
| `Images/Zadatak_4/Zadatak_4c_ASegmentControl.drawio` | `Images/Zadatak_4/Zadatak_4c_ASegmentControl.pdf` |
| `Images/Zadatak_4/Zadatak_4c_CompleteBCDLogic.drawio` | `Images/Zadatak_4/Zadatak_4c_CompleteBCDLogic.pdf` |
| `Images/Zadatak_4/Zadatak_4c_BCDComponent.drawio` | `Images/Zadatak_4/Zadatak_4c_BCDComponent.pdf` |
| `Images/Zadatak_4/Zadatak_4c_4Digits.drawio` | `Images/Zadatak_4/Zadatak_4c_4Digits.pdf` |

## Nekorišćeni grafički materijali

Sačuvani su; ne smatraju se delom konačnog studentskog PDF-a.
- `Images/MiddleComplexity/Comparator.drawio`
- `Images/MiddleComplexity/DEC.drawio`
- `Images/MiddleComplexity/MUX_4_1.drawio`
- `Images/Zadatak_2/Zadatak_2b.png`
- `Images/Zadatak_4/Zadatak_4clzout.drawio`

## VHDL izvori

Svih 20 fajlova obuhvaćeno je pregledom; GHDL ih prevodi u odvojenim privremenim direktorijumima.
- `code/Zadatak_1/a/tb_zadatak.vhd`
- `code/Zadatak_1/a/zadatak.vhd`
- `code/Zadatak_1/b/mux4.vhd`
- `code/Zadatak_1/b/tb_zadatak.vhd`
- `code/Zadatak_1/b/zadatak.vhd`
- `code/Zadatak_2/a/mux4.vhd`
- `code/Zadatak_2/a/tb_zadatak.vhd`
- `code/Zadatak_2/a/zadatak.vhd`
- `code/Zadatak_2/b/tb_zadatak.vhd`
- `code/Zadatak_2/b/zadatak.vhd`
- `code/Zadatak_2/d/tb_zadatak.vhd`
- `code/Zadatak_2/d/zadatak.vhd`
- `code/Zadatak_3/a/tb_zadatak.vhd`
- `code/Zadatak_3/a/zadatak.vhd`
- `code/Zadatak_3/b/decoder.vhd`
- `code/Zadatak_3/b/tb_zadatak.vhd`
- `code/Zadatak_3/b/zadatak.vhd`
- `code/Zadatak_3/c/decoder.vhd`
- `code/Zadatak_3/c/tb_zadatak.vhd`
- `code/Zadatak_3/c/zadatak.vhd`

Precizne lokacije i otisci izvora evidentiraju se u `../PROVERA/registar.json`. Završena provera sadržaja ne zamenjuje konačni vizuelni pregled svakog PDF lista.
