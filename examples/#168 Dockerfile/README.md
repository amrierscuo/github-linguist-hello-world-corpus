# #168 Dockerfile

Costruire ed eseguire un container che stampa Hello, World! con printf.

## Toolchain

Node.js v22.20.0; dockerfile-ast 0.7.1

## Comandi e procedura

npm install; node check.cjs; docker build -t linguist-hello-dockerfile .; docker run --rm linguist-hello-dockerfile

## Risultato atteso

Parser: FROM alpine:3.22.2 e CMD exec-form corretti; runtime previsto stdout Hello, World! più newline, exit 0.

## Stato

Sintassi verificata; semantica in attesa.

Parsing locale del Dockerfile con libreria comunitaria e parsing JSON nativo del CMD. Il daemon Docker non è attivo: nessun container è stato costruito o eseguito. La versione della base è esplicita; un futuro build richiederà accesso all’immagine Alpine. Nessuna pubblicazione prevista.

Verifica effettiva del 2026-10-08T12:00:44.301455+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

Requisiti residui:
- Docker Engine not running: named pipe dockerDesktopLinuxEngine absent; build/run pending.

## Fonti primarie e riferimento di formato

- [https://docs.docker.com/reference/dockerfile/](https://docs.docker.com/reference/dockerfile/)
- [https://github.com/rcjsuen/dockerfile-ast](https://github.com/rcjsuen/dockerfile-ast)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dockerfile` | [hello.dockerfile](variants/ext-dockerfile-2e646f636b657266696c65/hello.dockerfile) creato, verifiche pendenti |
| `.containerfile` | [hello.containerfile](variants/ext-containerfile-2e636f6e7461696e657266696c65/hello.containerfile) creato, verifiche pendenti |
