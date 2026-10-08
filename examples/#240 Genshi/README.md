# #240 Genshi

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare un template Genshi .kid con pubblico World e ottenere un paragrafo Hello, World!.

MarkupTemplate interpreta l’espressione py:content e il contesto audience=World. La stringa risultante sostituisce il placeholder del template. Il controllo confronta il markup realmente generato dal renderer originale.

## Toolchain e riproduzione

Genshi 0.7.11, CPython 3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

<p>Hello, World!</p>; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://genshi.edgewall.org/
- https://genshi.readthedocs.io/en/latest/templates.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.kid` | [hello.kid](hello.kid) verificato |
