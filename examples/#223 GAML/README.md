# #223 GAML

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Inizializzare un modello GAMA e scrivere Hello, World! nella console.

Il modello dichiara global/init e un esperimento GUI minimale. write usa la concatenazione GAML; non è un programma Java o un file di configurazione generico.

## Toolchain e riproduzione

GAMA Platform con runtime GAML; versione effettiva da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Aprire hello.gaml in GAMA, avviare l’esperimento greeting.
```

## Risultato atteso e stato

La sezione global/init scrive Hello, World! una volta.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: GAMA/Eclipse e runtime GAML non preparati; nessun parser o esperimento GAMA è stato eseguito.

## Fonti primarie

- https://gama-platform.org/wiki/Introduction
- https://gama-platform.org/wiki/next/ModelOrganization

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gaml` | [hello.gaml](hello.gaml) creato, verifiche pendenti |
