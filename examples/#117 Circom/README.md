# #117 Circom

Compilare un circuito Circom i cui 13 segnali pubblici di output sono i byte ASCII di Hello, World!, e calcolare il witness.

Tipo canonico: `programming`; `language_id`: `1042332086`.

Toolchain prevista: Circom 2.x e Node.js per il generatore di witness WASM. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
mkdir -p build
circom hello.circom --r1cs --wasm -o build
node build/hello_js/generate_witness.js build/hello_js/hello.wasm input.json build/hello.wtns
```

Risultato atteso: witness con constant one iniziale e output `[72,101,108,108,111,44,32,87,111,114,108,100,33]`; il vettore decodifica Hello, World!.

Il saluto è rappresentato come dati del circuito, non come stampa console. <== assegna i valori e genera i vincoli. Calcolo del witness e prova zero knowledge sono passaggi diversi; questo esempio non richiede un trusted setup.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Circom 2.2.3 linux/amd64 + Node.js 22.20.0 witness calculator. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [Circom — segnali e vincoli](https://docs.circom.io/circom-language/signals/)
- [Circom — implementazione originale](https://github.com/iden3/circom)

Verifica automatica inclusa: `node verify.cjs build/hello_js`.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.circom` | [hello.circom](hello.circom) verificato |
