# #479 Nunjucks

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare e renderizzare Nunjucks con audience=World.

Il motore originale Environment/FileSystemLoader analizza hello.njk, interpola audience e produce il markup. Il driver confronta l’HTML esatto.

## Toolchain e riproduzione

Nunjucks3.2.4, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
node render.js
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://mozilla.github.io/nunjucks/templating.html
- https://mozilla.github.io/nunjucks/api.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.njk` | [hello.njk](hello.njk) verificato |
