# #161 Daslang

Stampare Hello, World! e newline da main esportata in Daslang gen2.

## Toolchain

Official Daslang 0.6.4 Windows portable bundle

## Comandi e procedura

daslang --version; daslang hello.das

## Risultato atteso

Exit 0; stdout esattamente Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

La sintassi gen2 usa parentesi graffe e [export] per main. print non aggiunge newline: la sorgente lo specifica. Il bundle ufficiale contiene interprete e moduli; si usa il suo binario direttamente.

Verifica effettiva del 2026-10-08T11:56:15.636441+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://daslang.io/doc/reference/tutorials/01_hello_world.html](https://daslang.io/doc/reference/tutorials/01_hello_world.html)
- [https://github.com/GaijinEntertainment/daScript/releases/tag/v0.6.4](https://github.com/GaijinEntertainment/daScript/releases/tag/v0.6.4)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.das` | [hello.das](hello.das) verificato |
