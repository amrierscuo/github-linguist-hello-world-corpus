# #543 PogoScript

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare PogoScript e stampare Hello, World!.

Il CLI Pogo originale compila il file .pogo e lo esegue in Node. audience è una variabile del linguaggio, console.log è l’IO del backend JavaScript.

## Toolchain e riproduzione

Pogo0.10.0 ufficiale, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
pogo hello.pogo
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://featurist.github.io/pogoscript/
- https://github.com/featurist/pogoscript

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pogo` | [hello.pogo](hello.pogo) verificato |
