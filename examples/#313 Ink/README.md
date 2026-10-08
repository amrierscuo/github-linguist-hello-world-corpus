# #313 Ink

Compilare una storia Ink che emette Hello, World! e raggiunge END.

## Toolchain

Official inklecate v1.2.1 Windows release; generated inkVersion 21

## Comandi e procedura

inklecate -o build/hello.json hello.ink; inklecate -p hello.ink

## Risultato atteso

JSON della storia valido per Ink runtime; Play emette il saluto e finisce, exit 0.

## Stato

Sintassi e semantica verificate.

Entrambe le fasi usano il tool originale inklecate; il compiler e il runtime di Play sono reali. JSON compilato soltanto in work.

Verifica effettiva del 2026-10-08T12:29:57.976554+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://github.com/inkle/ink](https://github.com/inkle/ink)
- [https://github.com/inkle/ink/releases/tag/v1.2.1](https://github.com/inkle/ink/releases/tag/v1.2.1)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ink` | [hello.ink](hello.ink) verificato |
