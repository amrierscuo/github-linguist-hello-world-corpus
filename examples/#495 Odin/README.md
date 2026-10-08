# #495 Odin

Compilare ed eseguire Odin con fmt.println.

## Toolchain

<workspace>/work/tools_481_500/odin/odin-linux-amd64-nightly+2026-10-06/odin version dev-2026-10-nightly:84bc3fc; GCC linker

## Procedura

odin check hello.odin -file; odin build hello.odin -file -build-mode:obj -out:build/hello.o; gcc build/hello-*.o -lm -lpthread -o build/hello; build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:12:09.149453+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://odin-lang.org/docs/overview/](https://odin-lang.org/docs/overview/)
- [https://github.com/odin-lang/Odin/releases/tag/dev-2026-10](https://github.com/odin-lang/Odin/releases/tag/dev-2026-10)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.odin` | [hello.odin](hello.odin) verificato |
