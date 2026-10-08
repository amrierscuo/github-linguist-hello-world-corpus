# #381 Less

Compilare Less e renderizzare Hello, World! con un pseudo-elemento CSS.

## Toolchain

less 4.9.1; Node 22.20.0; Chrome 154.0.8037.98

## Comandi e procedura

npm install; npx lessc hello.less build/hello.css; copiare hello.html in build e aprirlo con Chrome; controllare #result

## Risultato atteso

content del ::before è Hello, World!; colore rgb(18, 69, 120); pass=true.

## Stato

Sintassi e semantica verificate.

Il file usa variabili Less, interpolazione e nesting. Il compilatore originale genera CSS; Chromium carica il CSS e controlla stile/computed content reale. hello.html è il consumer/checker; CSS compilato e profilo browser sono soltanto in work.

Verifica effettiva del 2026-10-08T12:49:26.160251+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://lesscss.org/usage/](https://lesscss.org/usage/)
- [https://lesscss.org/features/](https://lesscss.org/features/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.less` | [hello.less](hello.less) verificato |
