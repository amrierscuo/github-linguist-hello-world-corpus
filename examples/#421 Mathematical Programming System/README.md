# #421 Mathematical Programming System

Read a MPS model and solve variable 13 fixed to ASCII greeting codes.

Canonical type `programming`, language_id `429002699`.

Suggested toolchain: Python 3.13, highspy/HiGHS solver original.

From the example directory:

```sh
python verify.py
```

Expected result: accepted model, excellent solution and vector ASCII Hello, World!.

The file is a simple mathematical problem with bounds FX; the greeting is decoded by the solver solution, not read by a comment.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + HiGHS/highspy 1.15.1. [Log](verification/result.json).

Sources:

- [HiGHS — modello e solver](https://highs.dev/)
- [MPS — formato IBM CPLEX](https://www.ibm.com/docs/en/icos/22.1.2?topic=standard-records-in-mps-format)

Install the dependencies in a separate directory:

```sh
python -m pip install highspy==1.15.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mps` | [hello.mps](hello.mps) verified |
