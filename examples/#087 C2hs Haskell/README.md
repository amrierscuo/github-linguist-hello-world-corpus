# #087 C2hs Haskell

Risolvere con C2HS la costante C HELLO_SENTINEL=1 e stampare Hello, World! dal programma Haskell generato quando il valore è corretto.

## Riproduzione

Toolchain: C2HS 0.28.8; GHC 9.4.7. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
mkdir -p build
c2hs --cppopts=-I. Hello.chs -o build/Hello.hs
ghc build/Hello.hs -o build/hello
./build/hello
```

Risultato atteso: C2HS genera Haskell con costante 1; GHC compila; runtime stampa Hello, World!, exit 0.

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:34:12.651012+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://github.com/haskell/c2hs](https://github.com/haskell/c2hs)
- [https://github.com/haskell/c2hs/wiki/User-Guide](https://github.com/haskell/c2hs/wiki/User-Guide)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.chs` | [Hello.chs](Hello.chs) sintassi e semantica verificate |
