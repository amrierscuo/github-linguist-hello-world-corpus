# #554 Pro*C

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Precompilare Pro*C e stampare la variabile host greeting=Hello, World!.

EXEC SQL BEGIN/END DECLARE SECTION rende greeting una variabile host Pro*C. Il programma non richiede una query o una connessione Oracle per il saluto; il precompiler resta necessario per controllare le direttive.

## Toolchain e riproduzione

Oracle Pro*C/C++ precompiler e compiler C; versioni da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
proc iname=hello.pc; cc hello.c -o hello
```

```text
./hello
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Precompiler Oracle Pro*C non disponibile; GCC sul solo C non verifica le direttive EXEC SQL.

## Fonti primarie

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpcc/c-c-programmers-guide.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pc` | [hello.pc](hello.pc) creato, verifiche pendenti |
