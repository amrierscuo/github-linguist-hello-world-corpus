# #005 ABAP CDS

`zi_hello_world.ddls.asddls` definisce la view entity `ZI_Hello_World`: per ogni
cliente presente nella tabella SAP `T000` espone `Client` e il valore costante
`Hello, World!` nella colonna `Greeting`. È una definizione di dati, non un
programma che stampa su console. La lettura prevista non modifica `T000`.

## Toolchain e comandi

Parsing locale: **Node.js 22** e **abaplint 2.120.70**. Dalla cartella dell'esempio:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund @abaplint/cli@2.120.70
node .tools/node_modules/@abaplint/cli/abaplint abaplint.json -f json
```

La regola `cds_parser_error` controlla la grammatica DDL; risultato atteso:
codice 0 e `[]`. Il profilo `v758` è normalizzato da questo abaplint a `v793`
(on-premise 758), visibile nel log.

Verifica completa prevista: **SAP ABAP Platform con supporto alle view entity**,
tabella `T000` accessibile e **ABAP Development Tools (ADT)**. Creare una Data
Definition `ZI_HELLO_WORLD`, inserirvi il sorgente e usare `Activate` (Ctrl+F3).
Aprire `Data Preview` (F8) dell'entità attivata. Ogni riga deve avere
`Greeting = Hello, World!`. Non è richiesta una compilazione separata dall'attivazione.

L'oggetto ADT deve avere lo stesso nome della dichiarazione: `ZI_HELLO_WORLD`.
`T000` è una dipendenza del sistema classico; l'esempio non presume che sia
un'API rilasciata per ABAP Cloud.

## Stato e limiti

Sintassi **verificata dal parser CDS di abaplint**; semantica **non ancora
verificata**. `verification/abaplint.json` comprende un sorgente negativo
malformato, realmente respinto. La configurazione non risolve il dizionario
SAP e non attiva l'oggetto nel database. Manca il sistema SAP/ADT necessario
per completare la verifica.

## Fonti primarie

- [SAP, CDS view entity e loro impiego](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abencds_v2_views.htm).
- [SAP, regole DDL e stringhe tra apici singoli](https://help.sap.com/docs/ABAP_PLATFORM/f2e545608079437ab165c105649b89db/4ed24bd56e391014adc9fffe4e204223.html?version=1709.008).
- [abaplint, regole `cds_parser_error` e `cds_check_syntax`](https://rules.abaplint.org/).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asddls` | [zi_hello_world.ddls.asddls](zi_hello_world.ddls.asddls) sintassi verificata |
