# #099 CSV

Leggere con CSV il campo quotato Hello, World! senza dividerlo sulla virgola interna, poi riscrivere gli stessi dati con CRLF.

## Toolchain

Python 3.13.9; stdlib csv

## Comandi e procedura

Da questa cartella, senza dipendenze esterne:

```sh
python --version
python verify.py
```

Il saluto è tra doppi apici perché contiene una virgola. verify.py legge con
newline='' e csv.reader(strict=True), controlla tutte le celle e riscrive con
csv.writer e CRLF; confronta infine i byte con l'originale.

## Risultato atteso

Due righe e una colonna: intestazione greeting, valore Hello, World!; roundtrip byte per byte uguale al file originale UTF-8/CRLF.

## Stato

Sintassi e semantica verificate.

Parser csv standard in modalità strict, delimiter virgola e quotechar doppio apice. Il controllo comprende la virgola nel campo e i terminatori CRLF.

Verifica effettiva del 2026-10-08T11:33:46.142758+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://docs.python.org/3.13/library/csv.html](https://docs.python.org/3.13/library/csv.html)
- [https://www.rfc-editor.org/rfc/rfc4180](https://www.rfc-editor.org/rfc/rfc4180)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.csv` | [hello.csv](hello.csv) verificato |
