# #290 Handlebars

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare e renderizzare un template Handlebars con audience=World.

Il compiler Handlebars originale interpreta {{audience}} in modalità strict. La fixture fornisce il contesto e controlla il markup prodotto; le dipendenze sono isolate in work e il log conserva manifest e lockfile NPM.

## Toolchain e riproduzione

Handlebars4.7.8, Node.js22.20.0

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
node render.js
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://handlebarsjs.com/guide/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.handlebars` | [hello.handlebars](variants/handlebars-d5d95d20/hello.handlebars) creato, verifiche pendenti |
| `.hbs` | [hello.hbs](hello.hbs) verificato |
