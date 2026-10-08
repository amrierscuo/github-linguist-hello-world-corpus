# #648 Sass

Compilare Sass indentato in CSS con il saluto nel contenuto generato.

## Toolchain

Dart Sass 1.105.1; Node.js22.20.0; Chrome154.0.8037.98

## Procedura

npm install sass; node verify.cjs build/hello.css; copiare verify.html in build e aprirlo con Chrome; data-pass deve essere true

## Risultato atteso

CSS generato contiene #greeting::before e content: "Hello, World!".

## Stato

Sintassi e semantica verificate.

Compilatore Dart Sass originale e verifica del contenuto generato nel vero motore CSS Chromium; CSS/profilo browser restano in work.

Verifica reale 2026-10-08T13:24:10.648526+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://sass-lang.com/documentation/syntax/](https://sass-lang.com/documentation/syntax/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sass` | [hello.sass](hello.sass) verificato |
