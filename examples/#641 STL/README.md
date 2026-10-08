# #641 STL

Caricare una mesh STL originale che costruisce il saluto con pixel estrusi.

## Toolchain

Assimp 5.3.1 native STL importer

## Procedura

assimp info hello.stl; aprire in viewer 3D e verificare il saluto dall’alto.

## Risultato atteso

STL accettato; triangoli dei pixel estrusi mostrano Hello, World! dall’alto.

## Stato

Sintassi verificata; semantica in attesa.

Ogni pixel del font bitmap originale del corpus è un prisma chiuso; nessun modello/font esterno è copiato.

Verifica reale 2026-10-08T13:23:04.147430+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Visual inspection of original extruded greeting mesh pending.

## Fonti primarie

- [https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp](https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.stl` | [hello.stl](hello.stl) sintassi verificata |
