# #148 Cylc

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Definire un workflow Cylc a un ciclo con un task che stampa Hello, World!.

flow.cylc usa cycling mode integer e graph R1, con task runtime esplicito. La prova effettuata riguarda il validatore originale di configurazione e grafo. Per verificare la semantica di scheduling occorre eseguire install/play e controllare il job log; non si conteggia una semplice esecuzione manuale dello script shell.

## Toolchain e riproduzione

Cylc Flow 8.6.6; Python 3.12.3 su Ubuntu WSL

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
cylc validate .
cylc install . --workflow-name corpus-greeting
```

```text
cylc play corpus-greeting
```

## Risultato atteso e stato

Workflow valido; il job greeting/1 produce Hello, World! e il workflow conclude l’unico ciclo.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

Impedimenti: Cylc 8.6.6 avvia correttamente il CLI, ma validate non termina entro 90 secondi nel WSL. Il tentativo è registrato e il relativo processo è stato arrestato; scheduler e task non sono stati avviati.

## Fonti primarie

- https://cylc.github.io/cylc-doc/latest/html/tutorial/runtime/introduction.html
- https://github.com/cylc/cylc-flow

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cylc` | [flow.cylc](flow.cylc) creato, verifiche pendenti |
