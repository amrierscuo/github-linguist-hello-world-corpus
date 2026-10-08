# #200 FIGlet Font

Analizzare un font FIGlet originale a una riga e renderizzare Hello, World! mantenendo i singoli glifi.

Tipo canonico `data`, language_id `686129783`.

Toolchain prevista: Python 3 e pyfiglet.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: font caricato, altezza 1, rendering esatto `Hello, World!\n`.

I glifi e il commento del font sono originali: non viene redistribuito un font esterno. Sono presenti i 95 caratteri ASCII obbligatori e i sette caratteri tedeschi previsti dal formato; layout full-width senza smushing.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + pyfiglet 1.0.4. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [FIGfont — specifica originale](https://github.com/cmatsuoka/figlet/blob/master/figfont.txt)
- [pyfiglet — parser e renderer](https://github.com/pwaller/pyfiglet)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install pyfiglet==1.0.4
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.flf` | [greeting.flf](greeting.flf) verificato |
