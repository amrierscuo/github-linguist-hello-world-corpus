# #326 JSON5

Analizzare JSON5 con chiave non quotata, stringa con apici e virgola finale.

Canonical type `data`, language_id `175`.

Suggested toolchain: Python 3.13 and json5 library.

From the example directory:

```sh
python verify.py
```

Expected result: Hello, World! and LF; subject with proper greeting.

The artifact uses actual JSON5 characteristics.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + json5 0.16.0. [Log](verification/result.json).

Sources:

- [JSON5 — specifica](https://spec.json5.org/)
- [pyjson5 — implementazione](https://github.com/dpranke/pyjson5)

Install the dependencies in a separate directory:

```sh
python -m pip install json5==0.16.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.json5` | [hello.json5](hello.json5) verified |
