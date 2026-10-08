# #504 OpenQASM

Simulare un circuito OpenQASM 2 che prepara e misura i bit ASCII del saluto.

Tipo canonico `programming`, language_id `153739399`.

Toolchain prevista: Qiskit OpenQASM 2 parser e Aer stabilizer simulator.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: 104 misure deterministiche decodificate in Hello, World!.

X gates preparano stati della base computazionale; il simulatore stabilizer non alloca un vettore di 2^104 stati.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Qiskit 2.5.2 + qiskit-aer 0.17.2 native stabilizer simulator. [Log](verification/result.json). 

Fonti:

- [OpenQASM 2](https://github.com/openqasm/openqasm/tree/main/specs)
- [Qiskit qasm2](https://docs.quantum.ibm.com/api/qiskit/qasm2)
- [AerSimulator](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install qiskit==2.5.2 qiskit-aer==0.17.2
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qasm` | [hello.qasm](hello.qasm) verificato |
