# #368 LLVM TableGen

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Valutare un record LLVM TableGen e ottenere Text=Hello, World!.

La classe Greeting riceve audience, !strconcat costruisce il valore e def Hello specializza World. L’obiettivo è un record valutato dal vero TableGen, senza simulare un’architettura macchina.

## Toolchain e riproduzione

LLVM TableGen18.1.3

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
llvm-tblgen hello.td -print-records
```

## Risultato atteso e stato

Il record def Hello contiene string Text = "Hello, World!"; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://llvm.org/docs/TableGen/ProgRef.html
- https://llvm.org/docs/CommandGuide/tblgen.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.td` | [hello.td](hello.td) verificato |
