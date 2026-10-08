# #004 ABAP

`zhello_world.prog.abap` è un report eseguibile ABAP classico. `WRITE` inserisce
`Hello, World!` nella lista di output; `/` inizia una nuova riga.

## Toolchain e comandi

Controllo statico: **Node.js 22** e **abaplint 2.120.70**. Installazione locale
isolata, dalla cartella dell'esempio:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund @abaplint/cli@2.120.70
node .tools/node_modules/@abaplint/cli/abaplint abaplint.json -f json
```

La configurazione attiva `parser_error` e `check_syntax`. Il risultato atteso è
codice di uscita 0 e lista JSON vuota `[]`. Il target configurato `v758` viene
normalizzato da questa versione di abaplint al suo profilo `v793` (on-premise 758),
come riportato nel log.

Verifica nel runtime: creare il report `ZHELLO_WORLD` in un sistema **SAP AS ABAP
classico**, importare il sorgente, usare il controllo sintassi/attivazione e poi
`Execute` (F8) nell'ABAP Editor. La lista deve contenere `Hello, World!`.
Non è previsto un eseguibile locale da compilare separatamente.

## Stato e limiti

Sintassi **verificata staticamente** con abaplint; semantica di esecuzione
**non ancora verificata**. `verification/abaplint.json` registra anche un
controllo negativo: una stringa malformata è respinta dallo stesso analizzatore.
Non è disponibile un sistema SAP. Il controllo statico non costituisce
un'attivazione SAP né verifica il rendering della lista.

## Fonti primarie

- [SAP, istruzione `WRITE`](https://help.sap.com/docs/SAP_NETWEAVER_701/6da3d9466c4b1014a5a2e370bd8c5dc8/4a49ea1bea8b1c46e10000000a42189c.html).
- [SAP, programmi eseguibili e `REPORT`](https://help.sap.com/saphelp_scm700_ehp02/helpdata/en/fc/eb2d5a358411d1829f0000e829fbfe/content.htm?no_cache=true).
- [abaplint, progetto del verificatore](https://github.com/abaplint/abaplint).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.abap` | [zhello_world.prog.abap](zhello_world.prog.abap) sintassi verificata |
