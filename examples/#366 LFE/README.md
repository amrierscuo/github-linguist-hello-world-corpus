# #366 LFE

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare LFE in BEAM ed eseguire il saluto Hello, World!.

defmodule esporta main/0; io:format usa il formato ~s con una lista contenente World. Il compiler LFE originale è costruito dal sorgente Erlang autentico; BEAM esegue il modulo prodotto.

## Toolchain e riproduzione

LFE2.2.2, ErlangOTP25/ERTS13.2.2.5

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
lfec hello.lfe
```

```text
erl -noshell -pa . -eval "hello:main(), halt(0)."
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://lfe.io/learn/
- https://github.com/lfe/lfe/tree/v2.2.2

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lfe` | [hello.lfe](hello.lfe) verificato |
