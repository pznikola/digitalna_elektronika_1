# Otvorena stručna pitanja — predavanje 04

Datum: **2026-10-02**. Nijedna od sledećih stručnih ispravki nije primenjena. Izvorni zapisi ostaju na slajdovima. Predlozi, obrazloženja i zahtevi za odobrenje ostaju samo u ovoj tehničkoj evidenciji. Beleške su 2026-10-02 prepisane u nastavni tekst prema novom planu; ne sadrže otvorene predloge niti priču o odobravanju. Raspored svih slajdova je završen.

[PLAN_PREDAVANJA.md §1.1](../../../../PLAN_PREDAVANJA.md) propisuje: „Promene formula, vrednosti, topologije kola, stručnih tvrdnji ili uslova zahtevaju korisnikovo izričito odobrenje.“ Zato ove stavke ostaju nepotvrđene u sadržinskoj proveri.

| Slajd | Izvorni zapis i problem | Predložena stručna ispravka |
|---|---|---|
| s006 | 17/49 = 0.34693877551020408163265306122449…; poslednja cifra je zaokružena, iako se koristi znak nastavka. Isti niz javlja se dvaput. | Oba niza zameniti tačnim početkom **0.346938775510204081632653061224489795…**, uz postojeći celobrojni deo 167 gde postoji. |
| s009 | Iz CV/rⁿ < 1 izvedeno je n ≥ logᵣ CV. Za CV = 8, r = 2, n = 3 taj uslov dozvoljava nedovoljno cifara. | **n > logᵣ CV, za CV > 0**. Za CV = 0 predvideti jednu cifru; opšti postupak se ne menja. |
| s016 | Prvi indeksi su b_(n−1)(k−1), b_(n−1)(k−2), dok završni koriste dve oznake odvojene zarezom: b₀,₁ i b₀,₀. | Dosledno **b_(n−1,k−1)** i **b_(n−1,k−2)** za prve dve dvostruke oznake. Ne menjati grupisanje niti račun. |
| s034 | Decimalni primer 1000 − 123 = 877 nazvan je „komplement 9-tke“. Račun je za komplement osnove 10. | Promeniti samo naziv u **„komplement 10-tke“**. Rezultat 877 ostaje. |
| s035 | Druga formula oduzima invertovani zapis, pa dodaje 1, bez zagrada. Za 4 bita i V = 3 daje 16 − 12 + 1 = 5. | Oduzimati ceo komplement: **16 − (12 + 1) = 3**; u opštoj formuli dodati zagrade oko **invertovanog zapisa + 1**. |

Dovoljna je odluka da se navedene ispravke odobravaju, ili da se izvorni zapisi zadrže uz objašnjenja u beleškama. Stvarnu poruku evidentirati u [odluke.md](odluke.md). Agent ne sme sam izabrati tu stručnu odluku.

Posle odluke: primeniti samo odobrene izmene, prilagoditi beleške i odredišta sadržaja, ponovo pregledati pogođene slajdove i beleške, obnoviti njihove potvrde i pokrenuti `make -C predavanja LECTURE=04_brojni_sistemi check`. Tek zatim postaviti `ceka_odobrenje`. Odobrenje ovih ispravki nije prihvatanje završene 04 niti dozvola za 05.
