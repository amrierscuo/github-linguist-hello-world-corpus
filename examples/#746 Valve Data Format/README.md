# #746 Valve Data Format

Analyze Valve Data Format and read the message value.

Canonical type `data`, language_id `544060961`.

Suggested toolchain: Python3.13.9 + ValvePython vdf3.4.

From the example directory:

```sh
python verify.py
```

Expected result: KeyValues structure with greeting.

The text format KeyValues is used, not JSON.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + ValvePython vdf parser. [Log](verification/result.json).

Sources:

- [Valve KeyValues](https://developer.valvesoftware.com/wiki/KeyValues)
- [vdf parser](https://github.com/ValvePython/vdf)

Install the dependencies in a separate directory:

```sh
python -m pip install vdf
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vdf` | [hello.vdf](hello.vdf) verified |
| `.vmf` | [hello.vmf](variants/vmf-33d6e045/hello.vmf) created; verification pending |
