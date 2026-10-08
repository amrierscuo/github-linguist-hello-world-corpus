# #116 ChucK

Stampare il saluto tramite l’operatore di output diagnostico ChucK.

## Riproduzione

Toolchain: ChucK 1.5.2.1, silent mode. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
chuck --silent hello.ck
```

Risultato atteso: output diagnostico contenente la stringa `Hello, World!`, eventuali virgolette e annotazione del tipo string secondo la versione.

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:32:27.751792+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://chuck.cs.princeton.edu/doc/language/overview.html](https://chuck.cs.princeton.edu/doc/language/overview.html)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.ck` | [hello.ck](hello.ck) sintassi e semantica verificate |
