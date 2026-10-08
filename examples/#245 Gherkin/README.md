# #245 Gherkin

Eseguire uno scenario Gherkin che compone il saluto per il destinatario World.

## Toolchain

Node.js v22.20.0; official Cucumber.js 13.3.0

## Comandi e procedura

npm install; npx cucumber-js --require steps.cjs hello.feature

## Risultato atteso

Una scenario e tre step passed; Then confronta esattamente Hello, World!.

## Stato

Sintassi e semantica verificate.

steps.cjs è la glue necessaria alla semantica Gherkin. Il runner Cucumber originale interpreta Given/When/Then e il report JSON reale attesta tre step passed; nessun parser personalizzato.

Verifica effettiva del 2026-10-08T12:17:26.464731+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/)
- [https://github.com/cucumber/cucumber-js](https://github.com/cucumber/cucumber-js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.feature` | [hello.feature](hello.feature) verificato |
| `.story` | [hello.story](variants/ext-story-2e73746f7279/hello.story) creato, verifiche pendenti |
