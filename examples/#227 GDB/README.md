# #227 GDB

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire uno script di comandi GDB che stampa Hello, World!.

Il comando printf appartiene al linguaggio dei comandi GDB. -nx evita file di inizializzazione utente e -batch esegue soltanto lo script; non viene collegato o analizzato alcun processo esterno.

## Toolchain e riproduzione

GNU GDB 15.1, Ubuntu 15.1-1ubuntu1~24.04.1

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gdb -q -nx -batch -x hello.gdb
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.gnu.org/software/gdb/documentation/
- https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gdb` | [hello.gdb](hello.gdb) verificato |
| `.gdbinit` | [hello.gdbinit](variants/ext-gdbinit-2e676462696e6974/hello.gdbinit) creato, verifiche pendenti |
