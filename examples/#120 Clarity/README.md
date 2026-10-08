# #120 Clarity

Analizzare un contratto Clarity e chiamare localmente greeting, ottenendo la stringa ASCII Hello, World!.

Tipo canonico: `programming`; `language_id`: `91493841`.

Toolchain prevista: Clarinet o @stacks/clarinet-sdk con simulatore Clarity. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
node verify.cjs
```

Risultato atteso: valore Clarity (string-ascii 13) uguale a `Hello, World!`, senza modifiche di stato.

Il contratto espone una funzione read-only; la verifica usa soltanto un simulatore locale e non pubblica un contratto su Stacks.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Node.js 22.20.0 + @stacks/clarinet-sdk 3.24.1 + @stacks/transactions 7.6.0. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [Clarity — define-read-only](https://docs.stacks.co/reference/clarity)
- [Clarinet SDK — deployContract e callReadOnlyFn](https://docs.stacks.co/reference/clarinet-js-sdk/sdk-reference)

Verifica automatica inclusa: `node verify.cjs`.

Dipendenze riproducibili in una cartella di lavoro dedicata:

```sh
npm install --ignore-scripts --no-audit --no-fund @stacks/clarinet-sdk@3.24.1 @stacks/transactions@7.6.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.clar` | [hello.clar](hello.clar) verificato |
