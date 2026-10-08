# #039 AsciiDoc

Convertire il documento AsciiDoc con titolo Greeting e un paragrafo Hello, World! in HTML mantenendo il testo del paragrafo.

## File

- `hello.adoc`
- `check.cjs`
- `package.json`

## Toolchain e verifica

Node.js v22.20.0; @asciidoctor/core 4.1.1 (Asciidoctor.js).

Dalla cartella dell'esempio:

```sh
npm install
node check.cjs
```

`package.json` fissa `@asciidoctor/core` a 4.1.1. Il checker usa `await`
per parsing e conversione, come richiesto dall'API v4. Interroga l'albero
del documento e il risultato HTML; `MemoryLogger` cattura le diagnostiche.
L'HTML è controllato in memoria e non viene salvato come artefatto aggiuntivo.

## Risultato atteso

Titolo Greeting, esattamente un paragrafo Hello, World!, HTML contiene <p>Hello, World!</p>, zero diagnostiche ed exit 0.

## Stato della prova

Sintassi verificata. Semantica verificata.

Parsing e conversione HTML realmente eseguiti con API asincrona v4. HTML derivato controllato in memoria; nessun file .build consegnato.

Prova effettiva Windows x64 del 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
Il log include hash SHA-256 della sorgente, versioni osservate, comandi, codici di uscita, stdout e stderr.

## Fonti primarie

- [https://docs.asciidoctor.org/asciidoc/latest/](https://docs.asciidoctor.org/asciidoc/latest/)
- [https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/](https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/)
- [https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/](https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asciidoc` | [hello.asciidoc](variants/ext-asciidoc-2e6173636969646f63/hello.asciidoc) creato, verifiche pendenti |
| `.adoc` | [hello.adoc](hello.adoc) verificato |
| `.asc` | [hello.asc](variants/ext-asc-2e617363/hello.asc) creato, verifiche pendenti |
