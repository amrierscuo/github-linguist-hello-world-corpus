# #600 Raw token data

Decode a raw token dump Pygments and recover the token string value.

Canonical type `data`, language_id `318`.

Suggested toolchain: Python and Pygments RawTokenLexer.

From the example directory:

```sh
python verify.py
```

Expected result: a Literal.String token with Hello, World! value.

The Raw token entry is wide and does not define a pattern in the seed. The example explicitly chooses the raw token format documented by Pygments; the verification is valid for this variant.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + Pygments RawTokenLexer. [Log](verification/result.json).

Sources:

- [Pygments raw token format](https://pygments.org/docs/formatters/#RawTokenFormatter)
- [RawTokenLexer](https://github.com/pygments/pygments/blob/master/pygments/lexers/special.py)

Install the dependencies in a separate directory:

```sh
python -m pip install pygments
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.raw` | [hello.raw](hello.raw) verified |
