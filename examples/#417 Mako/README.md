# #417 Mako

Fill out a Mako template and replace targets with World.

Canonical type `programming`, language_id `221`.

Suggested toolchain: Python 3.13 and Mako.

From the example directory:

```sh
python verify.py
```

Expected result: stdout Hello, World! and LF, exit 0.

The engine generates and executes Python from the template; no simulated renderr.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + Mako 1.4.3. [Log](verification/result.json).

Sources:

- [Mako — manuale](https://docs.makotemplates.org/en/latest/syntax.html)

Install the dependencies in a separate directory:

```sh
python -m pip install mako==1.4.3
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mako` | [hello.mako](hello.mako) verified |
| `.mao` | [hello.mao](variants/mao-7fa3a20f/hello.mao) created; verification pending |
