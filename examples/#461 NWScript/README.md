# #461 NWScript

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire main NWScript e inviare Hello, World! al log tramite PrintString.

main concatena una stringa e chiama PrintString. Richiede le dichiarazioni builtin e la VM del gioco; GCC non è un compiler NWScript.

## Toolchain e riproduzione

Compiler e VM Neverwinter Nights/NWScript originali; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
Compilare hello.nss nel toolset NWN ed eseguirlo in un modulo locale.
```

## Risultato atteso e stato

Log del runtime contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Toolset/compiler/VM NWScript non preparati; verifiche pendenti.

## Fonti primarie

- https://forums.beamdog.com/uploads/editor/w4/7kqf0pqj21mb.pdf
- https://nwn.beamdog.net/docs/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nss` | [hello.nss](hello.nss) creato, verifiche pendenti |
