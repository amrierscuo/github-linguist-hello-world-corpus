# #630 SCSS

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare SCSS e ottenere un valore CSS content uguale a Hello, World!.

Il compilatore Sass valuta l’interpolazione nella stringa; la prova riguarda il CSS generato e non un browser.

## Toolchain e riproduzione

Dart Sass1.105.1 originale, Node22.20.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
sass hello.scss
```

## Risultato atteso e stato

CSS contiene content: "Hello, World!".

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://sass-lang.com/documentation/interpolation/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.scss` | [hello.scss](hello.scss) verificato |
