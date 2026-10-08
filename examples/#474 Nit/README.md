# #474 Nit

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare o compilare Nit e stampare Hello, World!.

La var audience viene interpolata nella stringa Nit con {audience}; print emette il saluto.

## Toolchain e riproduzione

Nit/nitc originali; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
nit hello.nit
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler/interprete Nit non preparato.

## Fonti primarie

- https://nitlanguage.org/tools/nit.html
- https://nitlanguage.org/doc/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nit` | [hello.nit](hello.nit) creato, verifiche pendenti |
