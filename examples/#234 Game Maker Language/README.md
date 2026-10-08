# #234 Game Maker Language

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire codice GML in un evento Create e mostrare Hello, World! nel log di GameMaker.

L’artefatto è codice Game Maker Language per il contesto di un evento, con variabile locale e show_debug_message. Il file non viene dichiarato come un progetto GameMaker completo.

## Toolchain e riproduzione

GameMaker IDE/runtime, versione effettiva da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Inserire hello.gml nell’evento Create di un oggetto in una room, poi eseguire il progetto.
```

## Risultato atteso e stato

Il debug log mostra Hello, World! una volta.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: IDE/runtime GameMaker non preparati; parser e creazione della room/evento non verificati.

## Fonti primarie

- https://manual.gamemaker.io/monthly/en/GameMaker_Language/GML_Reference/Debugging/show_debug_message.htm

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gml` | [hello.gml](hello.gml) creato, verifiche pendenti |
