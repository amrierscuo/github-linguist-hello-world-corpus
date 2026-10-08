# #621 Roc

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Roc e stampare Hello, World!.

main! usa la sintassi del nuovo compilatore descritta nel tutorial ufficiale. La release alpha4-rolling ottenuta contiene il compilatore storico, che richiede un header e non verifica questo sorgente.

## Toolchain e riproduzione

Roc nuovo compilatore con Echo platform builtin; tool provato: nightly d73ea109 del 09/09/2025

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
roc hello.roc
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Manca un binario del nuovo compilatore compatibile con il tutorial; tentativo reale incompatibile registrato.

## Fonti primarie

- https://raw.githubusercontent.com/roc-lang/roc/main/docs/mini-tutorial-new-compiler.md

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.roc` | [hello.roc](hello.roc) creato, verifiche pendenti |
