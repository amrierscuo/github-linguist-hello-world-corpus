# #713 Teal

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Controllare i tipi Teal, generare Lua ed eseguire Hello, World!.

Il compilatore Teal controlla l’annotazione string e genera il programma Lua poi realmente eseguito. La versione di sviluppo originale è identificata dal digest dell’archivio nel log.

## Toolchain e riproduzione

Teal originale dal repository teal-language/tl e Lua5.4.6

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
tl gen hello.tl; lua hello.lua
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://github.com/teal-language/tl

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tl` | [hello.tl](hello.tl) verificato |
