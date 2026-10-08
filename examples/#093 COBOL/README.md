# #093 COBOL

Stampare esattamente Hello, World! seguito da newline da un programma COBOL in formato libero.

## Toolchain

cobc (GnuCOBOL) 3.1.2.0

## Comandi e procedura

Con GnuCOBOL e la propria libreria libcob disponibili:

```sh
mkdir -p build
cobc --version
cobc -x -free -o build/hello hello.cob
./build/hello
```

Nel test i pacchetti sono stati estratti in una cartella work e invocati con
COB_CONFIG_DIR, COB_COPY_DIR, LD_LIBRARY_PATH e percorsi include/library
locali. In un'installazione normale questi percorsi sono già configurati.

## Risultato atteso

Compilazione e linking exit 0; programma exit 0, stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Toolchain GnuCOBOL ottenuta da pacchetti Ubuntu estratti localmente; nessuna installazione globale. Il compilatore C backend ha emesso un warning di ridefinizione _FORTIFY_SOURCE, conservato nel log; programma eseguito con successo.

Verifica effettiva del 2026-10-08T11:33:57.576818+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://gnucobol.sourceforge.io/doc/gnucobol.html](https://gnucobol.sourceforge.io/doc/gnucobol.html)
- [https://gnucobol.sourceforge.io/HTML/gnucobpg.html](https://gnucobol.sourceforge.io/HTML/gnucobpg.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cob` | [hello.cob](hello.cob), [consumer.cob](variants/ext-cpy-2e637079/consumer.cob) creato, verifiche pendenti |
| `.cbl` | [hello.cbl](variants/ext-cbl-2e63626c/hello.cbl) creato, verifiche pendenti |
| `.ccp` | [hello.ccp](variants/ext-ccp-2e636370/hello.ccp) creato, verifiche pendenti |
| `.cobol` | [hello.cobol](variants/ext-cobol-2e636f626f6c/hello.cobol) creato, verifiche pendenti |
| `.cpy` | [hello.cpy](variants/ext-cpy-2e637079/hello.cpy) creato, verifiche pendenti |
