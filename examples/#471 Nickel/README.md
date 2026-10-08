# #471 Nickel

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Valutare Nickel e ottenere il campo greeting=Hello, World!.

let lega audience e l’interpolazione %{audience} costruisce il campo del record. L’evaluator originale esporta il record JSON, confrontato con il valore atteso.

## Toolchain e riproduzione

Nickel1.18.0 ufficiale Windows

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nickel export --format json hello.ncl
```

## Risultato atteso e stato

JSON {"greeting":"Hello, World!"}; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://nickel-lang.org/user-manual/tutorial/
- https://github.com/tweag/nickel/releases/tag/1.18.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ncl` | [hello.ncl](hello.ncl) verificato |
