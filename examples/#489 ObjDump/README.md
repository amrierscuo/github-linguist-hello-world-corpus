# #489 ObjDump

Produrre una lista ObjDump autentica del programma C del saluto.

## Toolchain

GNU objdump (GNU Binutils for Ubuntu) 2.42; gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Procedura

gcc hello.c -o build/hello; (cd build && objdump -d -s hello > hello.objdump); build/hello; objcopy --dump-section .rodata=build/rodata.bin build/hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

hello.objdump è output testuale reale; l’ELF e la sezione binaria restano in work. Il saluto viene controllato nella sezione .rodata e nell’esecuzione del programma.

Verifica reale 2026-10-08T13:10:44.904153+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.objdump` | [hello.objdump](hello.objdump) verificato |
