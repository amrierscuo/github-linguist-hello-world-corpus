# #373 Lambdapi

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Definire in Lambdapi una lista di13numeri naturali che codifica ASCII Hello, World!.

Nat, zero, succ e List sono dichiarati nel file, senza librerie implicite. n32 ecc. definiscono numeri unari; greeting concatena i valori cons/nil. type e compute richiedono il motore di elaborazione originale.

## Toolchain e riproduzione

Lambdapi originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
lambdapi check hello.lp
```

```text
lambdapi check hello.lp
```

## Risultato atteso e stato

greeting è ben tipato; compute normalizza i13naturali72,101,108,108,111,44,32,87,111,114,108,100,33.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Lambdapi/ambiente OCaml non preparati; controllo del tipo e normalizzazione pendenti.

## Fonti primarie

- https://lambdapi.readthedocs.io/en/stable/commands.html
- https://lambdapi.readthedocs.io/en/stable/queries.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) creato, verifiche pendenti |
