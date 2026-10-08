# #362 KoLmafia ASH

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Interpretare KoLmafia ASH e stampare Hello, World!.

Il punto di ingresso main concatena una variabile string con print. La prova richiede il parser/interprete ASH della distribuzione KoLmafia.

## Toolchain e riproduzione

KoLmafia/ASH originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Nel CLI KoLmafia: call hello.ash
```

## Risultato atteso e stato

Console contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: KoLmafia non preparato; nessuna connessione al gioco effettuata.

## Fonti primarie

- https://github.com/kolmafia/kolmafia
- https://raw.githubusercontent.com/kolmafia/kolmafia/main/src/net/sourceforge/kolmafia/textui/Parser.java

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ash` | [hello.ash](hello.ash) creato, verifiche pendenti |
