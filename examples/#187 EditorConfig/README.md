# #187 EditorConfig

Resolve with EditorConfig the properties of the greeting.txt file and check the text and LF terminator.

Canonical type `data`, language_id `96139566`.

Suggested toolchain: Python 3 and editorconfig-core-py.

From the example directory:

```sh
python verify.py
```

Expected result: expected properties UTF - 8, LF, final newline and indentation of 2 spaces; preserved Hello, World! text.

The core solves the configuration; it does not apply changes as a editor would. The registered goal is the resolution of the properties and the comparison of the bytes of the file, not the integration with a IDE.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + editorconfig-core-py 0.17.1. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [EditorConfig — specifica e proprietà](https://editorconfig.org/)
- [EditorConfig core Python originale](https://github.com/editorconfig/editorconfig-core-py)

Install the dependencies in a separate directory:

```sh
python -m pip install editorconfig==0.17.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.editorconfig` | [.editorconfig](.editorconfig) verified |
