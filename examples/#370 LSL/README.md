# #370 LSL

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Al ricevimento di state_entry, comunicare Hello, World! al proprietario tramite LSL.

Lo stato default contiene un evento state_entry e chiama llOwnerSay; il saluto è codice eseguibile per il runtime LSL.

## Toolchain e riproduzione

Second Life/LSL o runtime compatibile; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Caricare hello.lsl come script di un oggetto e avviare state_entry.
```

## Risultato atteso e stato

Chat del proprietario contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Runtime LSL non disponibile; nessun accesso alla piattaforma online effettuato.

## Fonti primarie

- https://wiki.secondlife.com/wiki/LSL_Portal
- https://wiki.secondlife.com/wiki/LlOwnerSay

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lsl` | [hello.lsl](hello.lsl) creato, verifiche pendenti |
| `.lslp` | [hello.lslp](variants/lslp-5b201320/hello.lslp) creato, verifiche pendenti |
