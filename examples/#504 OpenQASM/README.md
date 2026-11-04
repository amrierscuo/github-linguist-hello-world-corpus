# #504 OpenQASM

Simulate an OpenQASM 2 circuit that prepares and measures the ASCII bits of greeting.

Canonical type `programming`, language_id `153739399`.

Suggested toolchain: Qiskit OpenQASM 2 parser and Aer stabilizer simulator.

From the example directory:

```sh
python verify.py
```

Expected result: 104 decoded deterministic measures in Hello, World!.

X gates prepare computational base states; the stabilizer simulator does not allocate a 2 vector 104 states.

Recorded status: syntax verified; behavior verified. Toolchain: Qiskit 2.5.2 + qiskit-aer 0.17.2 native stabilizer simulator. [Log](verification/result.json).

Sources:

- [OpenQASM 2](https://github.com/openqasm/openqasm/tree/main/specs)
- [Qiskit qasm2](https://docs.quantum.ibm.com/api/qiskit/qasm2)
- [AerSimulator](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)

Install the dependencies in a separate directory:

```sh
python -m pip install qiskit==2.5.2 qiskit-aer==0.17.2
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qasm` | [hello.qasm](hello.qasm) verified |
