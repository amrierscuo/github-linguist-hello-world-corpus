# #083 C

Stampare esattamente Hello, World! seguito da newline da un programma C11.

## Toolchain

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Comandi e procedura

Eseguire in Linux/WSL, creando una cartella temporanea di build:

```sh
mkdir -p build
gcc --version
gcc -std=c11 -Wall -Wextra -Werror -o build/hello hello.c
./build/hello
```

Il corpus consegnato contiene la sorgente e il log; l'eseguibile del test resta
in una cartella di lavoro esterna agli artefatti da pubblicare.

## Risultato atteso

Compilazione exit 0; programma exit 0 e stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Compilazione ed esecuzione reali con GCC; puts aggiunge il carattere newline.

Verifica effettiva del 2026-10-08T11:33:31.686254+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html](https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.c` | [hello.c](hello.c), [consumer.c](variants/ext-h-2e68/consumer.c), [consumer.c](variants/ext-h-in-2e682e696e/consumer.c) creato, verifiche pendenti |
| `.cats` | [hello.cats](variants/ext-cats-2e63617473/hello.cats) creato, verifiche pendenti |
| `.h` | [hello.h](variants/ext-h-2e68/hello.h) creato, verifiche pendenti |
| `.h.in` | [hello.h.in](variants/ext-h-in-2e682e696e/hello.h.in) creato, verifiche pendenti |
| `.idc` | [hello.idc](variants/ext-idc-2e696463/hello.idc) creato, verifiche pendenti |
