# #830 reStructuredText

Analizzare e renderizzare reStructuredText in HTML con enfasi.

## Toolchain

CPython3.13.9; Docutils0.23

## Procedura

pip install docutils; python verify.py

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Doctree e writer HTML5 sono quelli di Docutils originale; si confrontano testo del paragrafo e strong del saluto.

Verifica reale 2026-10-08T13:48:50.865932+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rst` | [hello.rst](hello.rst) verificato |
| `.rest` | [hello.rest](variants/rest-90077caa/hello.rest) creato, verifiche pendenti |
| `.rest.txt` | [hello.rest.txt](variants/rest-txt-4f6501d2/hello.rest.txt) creato, verifiche pendenti |
| `.rst.txt` | [hello.rst.txt](variants/rst-txt-05b28309/hello.rst.txt) creato, verifiche pendenti |
