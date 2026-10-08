# #363 Koka

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare Koka e stampare Hello, World!.

main usa val e concatenazione ++; il compiler originale effettua parsing, controllo dei tipi, compilazione C e link. Il binario è eseguito soltanto in work.

## Toolchain e riproduzione

Koka3.2.9, backend C e GCC

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
koka -o hello hello.kk
```

```text
./hello
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://koka-lang.github.io/koka/doc/book.html
- https://github.com/koka-lang/koka/releases/tag/v3.2.9

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kk` | [hello.kk](hello.kk) verificato |
