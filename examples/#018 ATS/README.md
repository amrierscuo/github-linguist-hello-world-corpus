# #018 ATS

Scrivere Hello World seguito da un a capo tramite main0 e println! in ATS2/Postiats.

## Riproduzione

Toolchain: ATS/Postiats 0.4.2; GCC 13.3.0. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
patscc -DATS_MEMALLOC_LIBC -o hello hello.dats
./hello
Per .hats/.sats compilare ed eseguire consumer.dats dalla relativa directory variants.
```

Risultato atteso: stdout: Hello World seguito da un a capo; exit 0.

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:32:26.148574+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html](https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html)
- [https://github.com/githwxi/ATS-Postiats](https://github.com/githwxi/ATS-Postiats)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.dats` | [hello.dats](hello.dats), [consumer.dats](variants/ext-hats-2e68617473/consumer.dats), [consumer.dats](variants/ext-sats-2e73617473/consumer.dats) sintassi e semantica verificate |
| `.hats` | [hello.hats](variants/ext-hats-2e68617473/hello.hats) sintassi e semantica verificate |
| `.sats` | [hello.sats](variants/ext-sats-2e73617473/hello.sats) sintassi e semantica verificate |
