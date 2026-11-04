# #507 OpenStep Property List

Analyze a property list OpenStep ASCII and read greeting.

Canonical type `data`, language_id `598917541`.

Suggested toolchain: Python and openstep-parser.

From the example directory:

```sh
python verify.py
```

Expected result: dictionary with Hello, World! value.

The format with brackets and cradle and comma is distinguished by XML and binary plist.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + openstep-parser 2.0.3. [Log](verification/result.json).

Sources:

- [OpenStep parser](https://github.com/kronenthaler/openstep-parser)

Install the dependencies in a separate directory:

```sh
python -m pip install openstep-parser==2.0.3
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.plist` | [hello.plist](hello.plist) verified |
| `.glyphs` | [hello.glyphs](variants/glyphs-cb9da07f/hello.glyphs) created; verification pending |
