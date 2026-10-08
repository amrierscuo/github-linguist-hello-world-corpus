# #022 Adobe Font Metrics

Voce canonica: `Adobe Font Metrics`, tipo `data`, `language_id: 147198098`.
`hello.afm` contiene metriche sintetiche originali in formato AFM 4.1 per i dieci
glifi distinti usati da `Hello, World!`. I codici dei glifi ricostruiscono il saluto;
la somma degli avanzamenti dei tredici caratteri deve essere **7500 unità**.

## Toolchain e riproduzione

Verificato su Windows x64 con Python **3.13.9** e **FontTools 4.60.1**.
Dalla directory di questo esempio:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install fonttools==4.60.1
.venv/Scripts/python.exe verify.py hello.afm
```

Per un ambiente Python che ha già FontTools 4.60.1: `python verify.py hello.afm`.
Risultato atteso: `Hello, World!` seguito da
`PASS: 10 glyph metrics; total advance = 7500 units; FontBBox = (0, 0, 600, 700)`.
Il programma usa `fontTools.afmLib.AFM` per leggere le metriche e controlla nome,
codici, larghezze e bounding box del file effettivo.

## Stato ed evidenza

Artefatto creato; sintassi **verificata**; semantica **verificata** con afmLib.
Controllo negativo reale: sostituendo il codice del glifo H con `broken`, il parser
genera `fontTools.afmLib.error` ed esce con codice 1. Il file è una dimostrazione di
metriche senza contorni; non è un font da usare per renderizzare il saluto.
La verifica copre il sottoinsieme AFM supportato da afmLib; la libreria dichiara
di non implementare l'intera specifica Adobe. Nessun requisito residuo per questa prova.

Log: [fonttools.json](verification/fonttools.json), con comandi, output, versioni e
SHA-256. `path_normalization` descrive la sostituzione dei percorsi della macchina;
i byte dei sorgenti e i risultati delle asserzioni restano invariati.

## Fonti ufficiali

- [FontTools afmLib: parser, accesso alle metriche e limiti](https://fonttools.readthedocs.io/en/latest/afmLib.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.afm` | [hello.afm](hello.afm) verificato |
