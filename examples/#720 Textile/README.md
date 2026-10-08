# #720 Textile

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Renderizzare Textile e leggere Hello, World! dal markup HTML.

Il renderer Textile autentico valuta il paragrafo e il grassetto. HTMLParser legge il testo dal risultato; non sostituisce il parser Textile.

## Toolchain e riproduzione

Python Textile4.0.4 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

HTML <p>Hello, <strong>World</strong>!</p>, testo Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://github.com/textile/python-textile

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.textile` | [hello.textile](hello.textile) verificato |
