# #157 DTrace

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Eseguire una clausola DTrace BEGIN che stampa Hello, World! e termina immediatamente.

L’estensione .d qui contiene il linguaggio D di DTrace, distinto dal linguaggio D generale. La sola sonda dtrace:::BEGIN viene eseguita all’avvio; non si raccolgono eventi o dati di altri processi. #pragma D option quiet elimina la tabella standard.

## Toolchain e riproduzione

DTrace originale su sistema supportato; versione effettiva da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
dtrace -e -s hello.d
```

```text
dtrace -s hello.d
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline; exit(0) chiude il programma DTrace.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: Runtime DTrace e supporto kernel non preparati in questo ambiente; compilazione e sonda BEGIN restano pendenti.

## Fonti primarie

- https://docs.oracle.com/cd/F61410_01/dtrace-guide/OL-DTRACE-GUIDE.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.d` | [hello.d](hello.d) creato, verifiche pendenti |
