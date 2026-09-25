# Status prenosa — 07

**31/31 slajdova** provereno sadržinski i vizuelno. Izvor ima 16 PDF strana,
poslednja samo gornji slajd; izlaz ima 31 stranu. Stroga provera prolazi.

Provereni su svi pasusi, formule, kod, legende i veze. PAL šema sadrži 32
kolone, 64 proizvodne linije, ulazne bafere, osam izlaznih grupa, povratne
veze i pripadajuće oznake. JEDEC slika ručno je prepisana, uključujući svih
352 prikazana bita; kod slajda 23 prenet je iako ga PDF tekstualni sloj ne sadrži.

Nezavisne provere obuhvataju 256 ulaznih kombinacija ABEL prioritetnog kodera,
četiri vektora I kola, 12 multiplekserskih test vektora, osam kombinacija
potpunog sabirača i kola sa slajda 21, i četiri događaja SR leča.
Sintaksni obrasci nisu proglašeni kompletnim izvršivim programima.

GHDL dodatno potvrđuje oscilaciju delta ciklusa izvornog VHDL prevoda na slajdu
27. Taj nalaz, pogrešni BIT literali i druge izvorne greške dokumentovani su
u `uocene_greske.md`, a izvorni prikaz nije prećutno ispravljen.
