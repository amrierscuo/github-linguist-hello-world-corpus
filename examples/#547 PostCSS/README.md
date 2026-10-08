# #547 PostCSS

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare PostCSS e risolvere una custom property nel valore content=Hello, World!.

Il sorgente .pcss definisce --greeting e la usa in content. Il parser e plugin originali trasformano il CSS; il driver legge il valore content dell’AST risultante. La prova verifica la trasformazione, senza attribuire un rendering browser.

## Toolchain e riproduzione

PostCSS8 e postcss-custom-properties originali; versioni effettive nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
node verify.js
```

## Risultato atteso e stato

CSS trasformato contiene content: "Hello, World!".

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://postcss.org/
- https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-custom-properties

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pcss` | [hello.pcss](hello.pcss) verificato |
| `.postcss` | [hello.postcss](variants/postcss-ca8f3f2b/hello.postcss) creato, verifiche pendenti |
