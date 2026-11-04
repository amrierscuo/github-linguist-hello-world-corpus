# #510 Org

Analyze an Org document and recover the title of the first node.

Canonical type `prose`, language_id `267`.

Suggested toolchain: Python and orgparse.

From the example directory:

```sh
python verify.py
```

Expected result: a heading with Hello, World! text.

The verification certifies the parsing of the Org structure, without declaring an Emacs export.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + orgparse 0.5.20260926. [Log](verification/result.json).

Sources:

- [Org syntax](https://orgmode.org/worg/dev/org-syntax.html)
- [orgparse](https://github.com/karlicoss/orgparse)

Install the dependencies in a separate directory:

```sh
python -m pip install orgparse
```

Install the dependencies in a separate directory:

```sh
python -m pip install orgparse==0.5.20260926
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.org` | [hello.org](hello.org) verified |
