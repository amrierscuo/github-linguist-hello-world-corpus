# #709 Tcl

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Tcl e stampare Hello, World!.

Interpolazione della variabile audience e puts del runtime Tcl autentico.

## Toolchain e riproduzione

Tcl8.6 originale, versione Ubuntu nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
tclsh hello.tcl
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.tcl-lang.org/man/tcl8.6/TclCmd/puts.htm

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tcl` | [hello.tcl](hello.tcl), [main.tcl](variants/tm-cb765f5d/main.tcl) creato, verifiche pendenti |
| `.adp` | [hello.adp](variants/adp-fdf7bf5a/hello.adp) creato, verifiche pendenti |
| `.sdc` | [hello.sdc](variants/sdc-c14a8049/hello.sdc) creato, verifiche pendenti |
| `.tcl.in` | [hello.tcl.in](variants/tcl-in-4fd82009/hello.tcl.in) creato, verifiche pendenti |
| `.tm` | [corpus-greeting-0.1.tm](variants/tm-cb765f5d/corpus-greeting-0.1.tm) creato, verifiche pendenti |
| `.xdc` | [hello.xdc](variants/xdc-305793a9/hello.xdc) creato, verifiche pendenti |
