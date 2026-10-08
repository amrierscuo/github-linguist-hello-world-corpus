# #633 SMT

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Risolvere un vincolo di stringa e leggere Hello, World! dal modello SMT.

SMT-LIB2 usa la teoria delle stringhe e str.++; Z3 produce sat e il valore della variabile greeting.

## Toolchain e riproduzione

Z3 solver5.1.0 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
z3 hello.smt2
```

## Risultato atteso e stato

sat e ((greeting "Hello, World!")).

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://smt-lib.org/theories-UnicodeStrings.shtml

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.smt2` | [hello.smt2](hello.smt2) verificato |
| `.smt` | [hello.smt](variants/smt-98f0359e/hello.smt) creato, verifiche pendenti |
| `.z3` | [hello.z3](variants/z3-f29d6e3b/hello.z3) creato, verifiche pendenti |
