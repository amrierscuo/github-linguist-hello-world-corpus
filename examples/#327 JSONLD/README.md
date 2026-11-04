# #327 JSONLD

Expand JSON - LD and associate Hello, World! to IRI greeting of the local context.

Canonical type `data`, language_id `176`.

Suggested toolchain: Python 3.13 and PyLD.

From the example directory:

```sh
python verify.py
```

Expected result: RDF expanded Hello, World! with expected IRI; stdout greeting and LF.

The context is embedded: no network requests are needed. example.invalid is used only as an identifier.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + PyLD 3.3.0. [Log](verification/result.json).

Sources:

- [W3C — JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
- [Digital Bazaar — PyLD](https://github.com/digitalbazaar/pyld)

Install the dependencies in a separate directory:

```sh
python -m pip install pyld==3.3.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jsonld` | [hello.jsonld](hello.jsonld) verified |
