# #467 NetLogo

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire la procedura greet di un modello NetLogo e stampare Hello, World!.

La procedura usa word e print; le sezioni .nlogo includono codice, info, versione e un esperimento BehaviorSpace originale. L’obiettivo è l’output della procedura, non il testo informativo del modello.

## Toolchain e riproduzione

NetLogo6.4.0 o versione compatibile; non preparato

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Aprire hello.nlogo in NetLogo e invocare greet.
```

## Risultato atteso e stato

Console del modello contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Loader/compiler/runtime NetLogo non preparati; modello non aperto.

## Fonti primarie

- https://docs.netlogo.org/dict/print.html
- https://raw.githubusercontent.com/NetLogo/models/6.4.0/Sample%20Models/Biology/Wolf%20Sheep%20Predation.nlogo

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nlogo` | [hello.nlogo](hello.nlogo) creato, verifiche pendenti |
