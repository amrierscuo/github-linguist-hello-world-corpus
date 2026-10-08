# #462 Nasal

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare Nasal nel runtime FlightGear e stampare Hello, World!.

La variabile audience è passata a print come argomento distinto; il builtin FlightGear concatena gli argomenti e scrive una linea.

## Toolchain e riproduzione

Nasal originale con funzione print del contesto FlightGear; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Caricare hello.nas nel contesto Nasal FlightGear.
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Nasal/FlightGear non preparati; runtime pendente.

## Fonti primarie

- https://wiki.flightgear.org/Creating_new_Nasal_scripts
- https://wiki.flightgear.org/Nasal_library

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nas` | [hello.nas](hello.nas) creato, verifiche pendenti |
