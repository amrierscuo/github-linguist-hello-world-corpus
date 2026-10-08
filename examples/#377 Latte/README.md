# #377 Latte

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare e renderizzare un template Latte con audience=World.

Il renderer usa Latte\Engine originale e renderToString. Il driver carica i file originali tramite autoload PSR4; il template è analizzato e compilato dal motore Latte, non sostituito manualmente.

## Toolchain e riproduzione

Latte3.0.26, PHP8.3.6 con tokenizer

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
php render.php
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://latte.nette.org/en/develop
- https://github.com/nette/latte/tree/v3.0.26

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.latte` | [hello.latte](hello.latte) verificato |
