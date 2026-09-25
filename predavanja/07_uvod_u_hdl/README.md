# Uvod u HDL

Izvor: `../07 Uvod u HDL.pdf`, 16 PDF strana i 31 slajd.
Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

Svih **31/31 slajdova** rekonstruisano je i pojedinačno sadržinski i vizuelno pregledano.

```sh
make -C predavanja LECTURE=07_uvod_u_hdl all
make -C predavanja LECTURE=07_uvod_u_hdl check
make -C predavanja LECTURE=07_uvod_u_hdl review
```

Izlaz: `build/07_uvod_u_hdl.pdf`. PAL matrica, kola i tokovi su uređivi TikZ izvori.
ABEL, VHDL i JEDEC primeri su tekstualni fajlovi u `kodovi`.
`provera_logike.py` nezavisno proverava tabele i logičke primere. GHDL nije obavezan
za izgradnju: njime je dodatno potvrđena izvorna greška sa slajda 27.
Greške i neizvršivi sintaksni obrasci originala ostaju preneti i odvojeno opisani
u `provera/uocene_greske.md`. Evidencija svih pregleda i otisaka je u `provera`.
