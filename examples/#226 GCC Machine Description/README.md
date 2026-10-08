# #226 GCC Machine Description

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Definire 13 costanti GCC Machine Description che codificano i byte di Hello, World!.

Il file usa il costrutto MD documentato define_constants, senza inventare pattern di istruzioni per una CPU. Il saluto è contenuto nei valori delle costanti. genconstants è uno strumento interno del build GCC; un compilatore gcc installato non equivale al parser MD.

## Toolchain e riproduzione

Generatori interni genconstants di un build tree GCC; versione effettiva da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
genconstants hello.md > greeting-constants.h
```

```text
Controllare CORPUS_CHAR_00..12 nell’header generato.
```

## Risultato atteso e stato

Le 13 macro emesse hanno i valori ASCII 72,101,108,108,111,44,32,87,111,114,108,100,33.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Un build tree GCC con il generatore genconstants non è disponibile; il file MD non è stato analizzato dal generatore originale.

## Fonti primarie

- https://gcc.gnu.org/onlinedocs/gcc-14.3.0/gccint/Machine-Desc.html
- https://gcc.gnu.org/onlinedocs/gcc-7.3.0/gccint/Constant-Definitions.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.md` | [hello.md](hello.md) creato, verifiche pendenti |
