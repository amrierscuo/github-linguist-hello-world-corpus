# #236 Gemini

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare un documento Gemini e ottenere il paragrafo Hello, World!.

Il documento contiene una heading di primo livello e un paragrafo gemtext. La libreria originale Gemtext restituisce tipi Heading/Paragraph; verify.py confronta le stringhe analizzate. Nessun server Gemini o richiesta di rete è necessario.

## Toolchain e riproduzione

gemtext 1.1.0, CPython 3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

PASS: Gemini paragraph = Hello, World!; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://geminiprotocol.net/docs/gemtext.gmi
- https://geminiprotocol.net/docs/gemtext-specification.gmi
- https://github.com/davep/gemtext

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gmi` | [hello.gmi](hello.gmi) verificato |
