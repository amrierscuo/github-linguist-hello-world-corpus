# #424 MeTTa

Execute a MeTTa expression that calls println! with greeting.

Canonical type `programming`, language_id `1037612668`.

Suggested toolchain: Python 3.13 and Hyperon MeTTa original.

From the example directory:

```sh
python verify.py
```

Expected result: stdout Hello, World! and LF, no MeTTa error.

The binding performs the original program with the standard engine library.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Hyperon — implementazione MeTTa](https://github.com/trueagi-io/hyperon-experimental)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.metta` | [hello.metta](hello.metta) created; verification pending |
