# #820 kvlang

Analizzare kvlang e mostrare una Label con il saluto.

## Toolchain

CPython3.13.9; Kivy2.3.1 Parser

## Procedura

pip install Kivy; python verify.py; caricare hello.kv con Builder in un’app Kivy e verificare la Label renderizzata.

## Risultato atteso

Hello, World!

## Stato

Sintassi verificata; semantica in attesa.

Il Parser originale può attestare la grammatica kvlang; un semplice esame della stringa non attesta il rendering.

Verifica reale 2026-10-08T13:38:35.604952+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Kivy Builder/native widget rendering pending.

## Fonti primarie

- [https://kivy.org/doc/stable/api-kivy.lang.html](https://kivy.org/doc/stable/api-kivy.lang.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kv` | [hello.kv](hello.kv) sintassi verificata |
