# #735 Unix Assembly

Assemblare sintassi GNU AT&T ed emettere il saluto tramite syscall Linux.

## Toolchain

GNU assembler (GNU Binutils for Ubuntu) 2.42

## Procedura

as -o build/hello.o hello.s; ld -o build/hello build/hello.o; build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:30:06.052119+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://sourceware.org/binutils/docs/as/](https://sourceware.org/binutils/docs/as/)
- [https://man7.org/linux/man-pages/man2/write.2.html](https://man7.org/linux/man-pages/man2/write.2.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.s` | [hello.s](hello.s) verificato |
| `.ms` | [hello.ms](variants/ms-5138d9ae/hello.ms) creato, verifiche pendenti |
