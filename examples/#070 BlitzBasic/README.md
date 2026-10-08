# #070 BlitzBasic

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Eseguire Print in BlitzBasic e visualizzare Hello, World!.

L’estensione .bb è condivisa con BitBake, ma questo file usa la sintassi BASIC di Blitz3D. Il sorgente non richiede grafica, media o risorse esterne.

## Toolchain e riproduzione

Blitz3D/BlitzBasic ufficiale per Windows; versione effettiva da registrare

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
Aprire hello.bb nell’IDE Blitz3D e usare Build and Run (F5).
```

```text
Eseguire il programma dalla stessa operazione dell’IDE.
```

## Risultato atteso e stato

La finestra di output mostra Hello, World!; programma terminato con End.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; nessun parser o runtime nativo è stato eseguito per questa voce.

Impedimenti: Compilatore/IDE Blitz3D non disponibile; build e output visuale restano da verificare nel software originale.

## Fonti primarie

- https://blitzresearch.itch.io/blitz3d
- https://github.com/blitz-research/blitz3d

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bb` | [hello.bb](hello.bb), [consumer.bb](variants/ext-decls-2e6465636c73/consumer.bb) creato, verifiche pendenti |
| `.decls` | [hello.decls](variants/ext-decls-2e6465636c73/hello.decls) creato, verifiche pendenti |
