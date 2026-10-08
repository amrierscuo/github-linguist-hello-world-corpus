# #180 Eagle

Aprire uno schematico EAGLE originale minimo con testo Hello, World! sul layer Info 97.

## Toolchain

Python 3.13.9; lxml 6.0.2; original EAGLE 7.7.0 vendor DTD mirrored in drtrigon/eagle

## Comandi e procedura

python -m pip install -r requirements.txt; python verify.py /percorso/eagle.dtd; aprire hello.sch in EAGLE/Fusion Electronics

## Risultato atteso

DTD valida lo schematico; nella CAD il testo appare sul layer Info.

## Stato

Sintassi verificata; semantica in attesa.

Lo schematico è un artefatto XML EAGLE con drawing/settings/grid/layers/schematic/sheets/plain/text, senza circuiti o componenti inventati. Il DTD originale del vendor è reperito in un mirror terzo ed è conservato solo in work con hash nel log. Il checker usa quel DTD completo, non una validazione personalizzata. L’apertura e la resa nella CAD restano da provare.

Verifica effettiva del 2026-10-08T12:01:47.817528+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

Requisiti residui:
- Autodesk EAGLE/Fusion Electronics CAD opening and visual text check not performed.

## Fonti primarie e riferimento di formato

- [https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm](https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm)
- [https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch](https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch)
- [https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd](https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sch` | [hello.sch](hello.sch) sintassi verificata |
| `.brd` | [hello.brd](variants/ext-brd-2e627264/hello.brd) creato, verifiche pendenti |
