# #092 CMake

Eseguire in CMake script mode un controllo sul valore greeting e scrivere Hello, World! con message.

## Toolchain

cmake version 4.4.4

## Comandi e procedura

Non serve un progetto o un compilatore C/C++; usare la modalità script:

```sh
cmake --version
cmake -P hello.cmake
```

Il saluto compare su stderr. Un errore sul valore della variabile sarebbe
segnalato da FATAL_ERROR e produrrebbe un esito di comando diverso da zero.

## Risultato atteso

Exit 0; stderr contiene esattamente Hello, World! più newline; stdout vuoto.

## Stato

Sintassi e semantica verificate.

message senza modo STATUS invia il messaggio a stderr: il canale corretto è esplicitamente verificato. Il controllo if/FATAL_ERROR è eseguito dal vero CMake.

Verifica effettiva del 2026-10-08T11:33:20.658387+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://cmake.org/cmake/help/latest/manual/cmake.1.html](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
- [https://cmake.org/cmake/help/latest/command/message.html](https://cmake.org/cmake/help/latest/command/message.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cmake` | [hello.cmake](hello.cmake), [configure.cmake](variants/ext-cmake-in-2e636d616b652e696e/configure.cmake) creato, verifiche pendenti |
| `.cmake.in` | [hello.cmake.in](variants/ext-cmake-in-2e636d616b652e696e/hello.cmake.in) creato, verifiche pendenti |
