# #293 Haskell

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Interpretare Haskell98 e stampare il valore greeting = Hello, World!.

Il modulo Main dichiara greeting::String e main::IO(). ++ concatena stringhe e putStrLn realizza l’IO. Il test usa l’interprete Haskell autentico Hugs in modalità +98, con HUGSDIR e search path delle librerie isolati.

## Toolchain e riproduzione

Hugs98 September2006, pacchetto98.200609.21-6build3 e librerie bundled Ubuntu

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
runhugs +98 Hello.hs
```

## Risultato atteso e stato

stdout esattamente Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.haskell.org/hugs/
- https://www.haskell.org/onlinereport/haskell2010/haskellch9.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hs` | [Hello.hs](Hello.hs), [Greeting.hs](variants/hs-boot-9862d855/Greeting.hs), [Audience.hs](variants/hs-boot-9862d855/Audience.hs), [Main.hs](variants/hs-boot-9862d855/Main.hs) creato, verifiche pendenti |
| `.hs-boot` | [Greeting.hs-boot](variants/hs-boot-9862d855/Greeting.hs-boot) creato, verifiche pendenti |
| `.hsc` | [hello.hsc](variants/hsc-700d6b1e/hello.hsc) creato, verifiche pendenti |
