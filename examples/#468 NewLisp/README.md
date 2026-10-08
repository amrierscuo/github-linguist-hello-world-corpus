# #468 NewLisp

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare newLISP e stampare Hello, World!.

set lega audience; string costruisce il saluto, println realizza l’IO ed exit0 termina il programma. La prova usa l’interprete newLISP autentico.

## Toolchain e riproduzione

newLISP10.7.5 Linux ufficiale Ubuntu

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
newlisp hello.nl
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.newlisp.org/downloads/newlisp_manual.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nl` | [hello.nl](hello.nl) verificato |
| `.lisp` | [hello.lisp](variants/lisp-757ceb1b/hello.lisp) creato, verifiche pendenti |
| `.lsp` | [hello.lsp](variants/lsp-270be2e4/hello.lsp) creato, verifiche pendenti |
