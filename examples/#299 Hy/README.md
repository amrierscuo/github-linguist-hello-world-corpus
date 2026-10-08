# #299 Hy

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare ed eseguire Hy per stampare Hello, World!.

La forma setv lega greeting al risultato della concatenazione prefissa; print usa il builtin Python dal linguaggio Hy. La verifica passa attraverso il CLI/compiler Hy autentico e la VM Python risultante.

## Toolchain e riproduzione

Hy1.3.1, funcparserlib1.0.1, CPython3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
hy hello.hy
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://hylang.org/hy/doc/v1.1.0/tutorial
- https://github.com/hylang/hy

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hy` | [hello.hy](hello.hy) verificato |
