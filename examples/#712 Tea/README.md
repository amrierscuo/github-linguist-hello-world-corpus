# #712 Tea

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Renderizzare un template Tea con parametro audience = World.

Template Tea nel sistema Java TeaTrove: la regione testo e l’espressione audience producono il saluto.

## Toolchain e riproduzione

Tea compiler/runtime TeaTrove, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
TeaTrove: compilare hello.tea e invocare hello con parametro World
```

## Risultato atteso e stato

Hello, World! con newline finale.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: TeaTrove compiler/runtime non disponibili; parser e rendering pendenti.

## Fonti primarie

- https://github.com/teatrove/teatrove/wiki/Tea-Templates

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tea` | [hello.tea](hello.tea) creato, verifiche pendenti |
