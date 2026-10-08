# #250 Gleam

Compilare e tipizzare un main Gleam che stampa Hello, World! tramite gleam/io.

## Toolchain

gleam 1.19.1; Node.js 22.20.0; Hex dependencies in real manifest.toml

## Comandi e procedura

gleam --version; gleam check; gleam run --target javascript --runtime node

## Risultato atteso

Type check e build senza errori; stdout Hello, World! più newline, exit 0.

## Stato

Sintassi e semantica verificate.

Il compilatore ufficiale emette JavaScript per Node; il programma usa la libreria standard reale. manifest.toml è generato dal tool con versione e checksum Hex effettivi. Build/cache restano in work; il backend Erlang non è stato provato.

Verifica effettiva del 2026-10-08T12:15:38.798185+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://gleam.run/](https://gleam.run/)
- [https://tour.gleam.run/basics/hello-world/](https://tour.gleam.run/basics/hello-world/)
- [https://gleam.run/writing-gleam/command-line-reference/](https://gleam.run/writing-gleam/command-line-reference/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gleam` | [hello_world_corpus.gleam](src/hello_world_corpus.gleam) verificato |
