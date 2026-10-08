# #759 Vyper

Compilare Vyper ed eseguire la funzione pura greeting in un EVM isolato.

Tipo canonico `programming`, language_id `1055641948`.

Toolchain prevista: Vyper0.4.3 + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: Original Vyper compiler produces ABI/bytecode; in-memory EVM returns ABI string Hello, World!.

L’esecuzione prevista è in memoria, senza blockchain esterne.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Original Solidity solc0.8.37 or Vyper0.4.3 compiler + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM. [Log](verification/result.json). 

Fonti:

- [Vyper](https://docs.vyperlang.org/en/stable/)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install vyper==0.4.3
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
| `.vy` | [hello.vy](hello.vy) verificato |
