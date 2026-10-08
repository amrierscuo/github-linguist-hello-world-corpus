# #426 Mermaid

Analizzare un diagramma Mermaid e leggere l’etichetta del nodo greeting dal database del parser.

Tipo canonico `markup`, language_id `385992043`.

Toolchain prevista: Node.js 22, Mermaid e jsdom.

Dalla cartella dell’esempio:

```sh
node verify.cjs
```

Risultato atteso: un nodo greeting con testo Hello, World!; stdout saluto e LF.

L’obiettivo è l’interpretazione del grafo e dell’etichetta con il motore originale. Non certifica geometria SVG o rendering di un browser.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + Mermaid 11.12.0 + jsdom 26.1.0. [Log](verification/result.json). 

Fonti:

- [Mermaid — flowchart](https://mermaid.js.org/syntax/flowchart.html)
- [Mermaid — API](https://mermaid.js.org/config/usage.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund mermaid@11.12.0 jsdom@26.1.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mmd` | [hello.mmd](hello.mmd) verificato |
| `.mermaid` | [hello.mermaid](variants/mermaid-4637b47f/hello.mermaid) creato, verifiche pendenti |
