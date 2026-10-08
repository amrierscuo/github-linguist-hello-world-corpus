# #387 Linker Script

Collocare la stringa Hello, World! in una sezione ELF tramite un linker script originale.

## Toolchain

GNU ld (GNU Binutils for Ubuntu) 2.42; GCC 13.3.0

## Comandi e procedura

gcc main.c -Wl,-T,hello.ld -o build/hello; readelf -p .greeting build/hello; build/hello

## Risultato atteso

Sezione .greeting contiene il testo; boundary symbols racchiudono 14 byte; runtime stampa il saluto.

## Stato

Sintassi e semantica verificate.

INSERT AFTER .rodata integra lo script nel layout standard ELF. KEEP conserva la sezione e il programma usa davvero __greeting_start; non stampa una seconda stringa indipendente dal linker. Nessun ELF consegnato.

Verifica effettiva del 2026-10-08T12:48:20.800152+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://sourceware.org/binutils/docs/ld/SECTIONS.html](https://sourceware.org/binutils/docs/ld/SECTIONS.html)
- [https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html](https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ld` | [hello.ld](hello.ld) verificato |
| `.lds` | [hello.lds](variants/lds-ad88c9e8/hello.lds) creato, verifiche pendenti |
| `.x` | [hello.x](variants/x-bb42e4c6/hello.x) creato, verifiche pendenti |
