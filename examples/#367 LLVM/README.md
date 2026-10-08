# #367 LLVM

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Assemblare LLVM IR ed eseguire main che stampa Hello, World! tramite puts.

L’array di14byte include terminatore NUL. main chiama puts con un puntatore LLVM e restituisce0; llvm-as controlla IR e tipi, lli esegue il codice con JIT nativo.

## Toolchain e riproduzione

LLVM18.1.3 Ubuntu, llvm-as e lli

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
llvm-as hello.ll -o hello.bc
```

```text
lli hello.bc
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://llvm.org/docs/LangRef.html
- https://llvm.org/docs/CommandGuide/lli.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ll` | [hello.ll](hello.ll) verificato |
