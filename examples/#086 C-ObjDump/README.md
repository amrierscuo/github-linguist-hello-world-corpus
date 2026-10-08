# #086 C-ObjDump

Conservare un disassemblato C-ObjDump autentico del programma C che stampa Hello, World!, includendo le righe C e le istruzioni di main.

## Toolchain

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 / GNU objdump (GNU Binutils for Ubuntu) 2.42

## Comandi e procedura

Rigenerazione con toolchain ELF x86_64 Linux/WSL:

```sh
mkdir -p build
gcc -std=c11 -Wall -Wextra -Werror -g -O0 -fno-pie -no-pie -o build/hello hello.c
objdump --version
objdump -d -S build/hello > build/hello.c-objdump
./build/hello
```

Il listing consegnato è una prova prodotta dal tool. Gli indirizzi e i dettagli
del compilatore possono cambiare tra toolchain; la sorgente di main e il
saluto restano riconoscibili. I percorsi delle sorgenti sono normalizzati per
pubblicare un artefatto leggibile senza riferimenti alla macchina locale.

## Risultato atteso

Objdump exit 0; testo contiene main, istruzioni e sorgente puts("Hello, World!"); programma C stampa il saluto, exit 0.

## Stato

Sintassi e semantica verificate.

hello.c-objdump è prodotto da objdump, non scritto a mano. I percorsi assoluti delle sorgenti sono normalizzati con <corpus>; formato e istruzioni restano quelli del tool. Il listing è un formato dati; la prova di esecuzione riguarda l'ELF C corrispondente, conservato solo in work.

Verifica effettiva del 2026-10-08T11:33:36.476099+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.c-objdump` | [hello.c-objdump](hello.c-objdump) verificato |
