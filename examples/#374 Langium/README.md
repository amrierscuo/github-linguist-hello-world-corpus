# #374 Langium

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Generare un parser da una grammatica Langium e riconoscere Hello, World!.

La grammatica definisce entry Model, ID e whitespace nascosto. createServicesForGrammar analizza il sorgente e costruisce il parser originale; la fixture Hello, World! è realmente analizzata.

## Toolchain e riproduzione

Langium4.4.0/Chevrotain, Node22.20; versione effettiva nel log

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
node verify.mjs
```

## Risultato atteso e stato

Nessun lexer/parser error; AST Model con audience=World.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://langium.org/docs/reference/grammar-language/
- https://github.com/eclipse-langium/langium

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.langium` | [hello.langium](hello.langium) verificato |
