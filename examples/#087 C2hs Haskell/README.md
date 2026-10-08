# #087 C2hs Haskell

Risolvere con C2HS la costante C HELLO_SENTINEL=1 e stampare Hello, World! dal programma Haskell generato quando il valore è corretto.

## Toolchain

C2HS 0.28.8; GCC C preprocessor; GHC runtime not installed

## Comandi e procedura

hello.h definisce una costante C originale; l'hook `{#const ... #}` la
risolve nel testo Haskell generato. Eseguire nella cartella dell'esempio:

```sh
mkdir -p build
c2hs --version
c2hs Hello.chs -o build/Hello.hs
ghc build/Hello.hs -o build/hello
./build/hello
```

La prova registrata si ferma dopo C2HS, perché GHC non è presente. Il saluto
nel file generato non è stato eseguito; per questo la semantica resta in attesa.

## Risultato atteso

C2HS genera Haskell con costante 1; GHC compila; runtime stampa Hello, World!, exit 0.

## Stato

Sintassi verificata; semantica in attesa.

Il preprocessore C2HS reale accetta il binding e risolve l'hook const. Il codice Haskell ospite è preservato dal preprocessore: parsing/compilazione Haskell ed esecuzione con GHC restano da verificare.

Verifica effettiva del 2026-10-08T11:33:13.575372+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

Requisiti residui:
- GHC absent: compile and execute generated Haskell to complete the greeting runtime proof.

## Fonti primarie

- [https://github.com/haskell/c2hs](https://github.com/haskell/c2hs)
- [https://github.com/haskell/c2hs/wiki/User-Guide](https://github.com/haskell/c2hs/wiki/User-Guide)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.chs` | [Hello.chs](Hello.chs) sintassi verificata |
