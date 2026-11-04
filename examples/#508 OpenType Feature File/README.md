# #508 OpenType Feature File

Fill out an OpenType Feature File statement in the name table of a font.

Canonical type `data`, language_id `374317347`.

Suggested toolchain: Python and fontTools feaLib.

From the example directory:

```sh
python verify.py
```

Expected result: name ID 4 built by the compiler and equal to greeting.

Greeting is the full font name; the fixture does not demand a font with glifi drawn.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + fontTools 4.66.1 feaLib. [Log](verification/result.json).

Sources:

- [fontTools feaLib](https://fonttools.readthedocs.io/en/latest/feaLib/index.html)
- [Adobe feature file specification](https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html)

Install the dependencies in a separate directory:

```sh
python -m pip install fonttools
```

Install the dependencies in a separate directory:

```sh
python -m pip install fonttools==4.66.1
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fea` | [hello.fea](hello.fea) verified |
