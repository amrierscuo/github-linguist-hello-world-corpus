# #088 C3

Stampare esattamente Hello, World! seguito da newline con std::io in C3.

## Toolchain

C3 0.8.4 / LLVM 22.1.8 (Windows)

## Comandi e procedura

Con la distribuzione ufficiale C3 0.8.4, dalla cartella dell'esempio:

```text
c3c --version
c3c compile hello.c3 -o hello
hello.exe
```

Su Linux/macOS l'ultimo comando è `./hello`. Per tenere separati i derivati,
il test ha compilato una copia della sorgente in una cartella work e ha
registrato l'hash della sorgente originale consegnata.

## Risultato atteso

Compilatore e linker exit 0; eseguibile exit 0 e stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Compilazione, linking ed esecuzione realmente svolti con il compilatore ufficiale C3 portable Windows. Eseguibile mantenuto in work.

Verifica effettiva del 2026-10-08T11:34:07.737503+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://c3-lang.org/getting-started/hello-world/](https://c3-lang.org/getting-started/hello-world/)
- [https://github.com/c3lang/c3c/releases/tag/v0.8.4](https://github.com/c3lang/c3c/releases/tag/v0.8.4)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.c3` | [hello.c3](hello.c3) verificato |
