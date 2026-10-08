# #399 LookML

Descrivere una derived table LookML che restituisce il saluto come dimensione stringa.

## Toolchain

Community lkml 1.3.7 genuine LookML parser; SQLite 3.51.0; Python 3.13.9

## Comandi e procedura

python -m pip install -r requirements.txt; python verify.py; caricare view nel progetto Looker di prova ed eseguire query della dimensione greeting

## Risultato atteso

Parser accetta view/derived_table/dimension; SQL restituisce il saluto; Looker deve validare e interrogare la dimensione.

## Stato

Sintassi verificata; semantica in attesa.

lkml è un parser community esistente, non un validatore implementato qui. SQLite esegue il SQL estratto dal vero AST e trova il saluto. La sostituzione ${TABLE}, connessione e semantica Looker restano pending.

Verifica effettiva del 2026-10-08T12:49:21.017261+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Google Looker project/database connection and native validator/runtime pending.

## Fonti primarie

- [https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table)
- [https://github.com/joshtemple/lkml](https://github.com/joshtemple/lkml)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lkml` | [hello.view.lkml](hello.view.lkml) sintassi verificata |
| `.lookml` | [hello.lookml](variants/lookml-1f224142/hello.lookml) creato, verifiche pendenti |
