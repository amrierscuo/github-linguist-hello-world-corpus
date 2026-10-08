# #224 GAMS

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire GAMS e scrivere Hello, World! nel file greeting.txt.

Il sorgente usa un file GAMS, put e putclose. Il risultato è un file di testo, non l’output di un solver: non viene definito un modello di ottimizzazione.

## Toolchain e riproduzione

GAMS, installazione e licenza adatte; versione effettiva da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
gams hello.gms
```

## Risultato atteso e stato

greeting.txt contiene Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Runtime proprietario GAMS non preparato; parsing ed esecuzione put restano pendenti.

## Fonti primarie

- https://www.gams.com/53/docs/UG_Put.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gms` | [hello.gms](hello.gms) creato, verifiche pendenti |
