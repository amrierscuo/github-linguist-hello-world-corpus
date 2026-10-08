# #674 Solidity

Compilare un contratto Solidity con funzione pura che restituisce il saluto.

Tipo canonico `programming`, language_id `237469032`.

Toolchain prevista: Solidity solc0.8.37 + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM.

Dalla cartella dell’esempio:

```sh
mkdir -p build
node verify.cjs build/contract.json
python verify_evm.py build/contract.json
```

Risultato atteso: Original compiler produces bytecode; local in-memory EVM call returns ABI string Hello, World!; stdout greeting and newline.

La compilazione è distinta dall’esecuzione. Non vengono creati account o transazioni su reti blockchain.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Original Solidity solc0.8.37 or Vyper0.4.3 compiler + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM. [Log](verification/result.json). 

Fonti:

- [Solidity](https://docs.soliditylang.org/en/latest/)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install solc
```

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install eth-tester[py-evm] vyper==0.4.3
```

Verifica completa eseguita: deploy su PyEVM in memoria, transazione locale e chiamata greeting; valore string decodificato dall’ABI e confrontato con Hello, World!. Non è stata usata una rete blockchain esterna.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sol` | [Hello.sol](Hello.sol) verificato |
