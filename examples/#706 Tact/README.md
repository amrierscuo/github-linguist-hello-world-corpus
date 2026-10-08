# #706 Tact

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare un contratto Tact il cui getter restituisce Hello, World!.

La toolchain Tact/FunC originale compila davvero il contratto e produce bytecode TON nelle cartelle temporanee. Nessun contratto viene distribuito.

## Toolchain e riproduzione

Tact compiler1.6.13 originale, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
tact --config tact.config.json
```

## Risultato atteso e stato

Compilazione exit0; greeting() atteso Hello, World! dopo esecuzione in VM.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Getter non eseguito in VM TON; semantica runtime pendente.

## Fonti primarie

- https://docs.tact-lang.org/book/contracts/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tact` | [hello.tact](hello.tact) sintassi verificata |
