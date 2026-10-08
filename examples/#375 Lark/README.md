# #375 Lark

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Costruire un parser LALR Lark e riconoscere Hello, World!.

Il motore Lark originale interpreta hello.lark e costruisce il parser LALR. I token dell’albero vengono confrontati dalla fixture Python; il driver non implementa un parser sostitutivo.

## Toolchain e riproduzione

Lark1.3.1, CPython3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Albero start con token Hello e World; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://lark-parser.readthedocs.io/en/latest/grammar.html
- https://github.com/lark-parser/lark

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lark` | [hello.lark](hello.lark) verificato |
