# #109 Cap'n Proto

Analyze a Cap’n Proto scheme, create Greeting with the default value and store it in a serializzazione/lettura. cycle

Canonical type: `programming`; `language_id`: `52`.

Suggested toolchain: Python 3 and pycapnp (binding parser/runtime C++ Cap’n Proto).

From the example folder, depending on the PATH:

```sh
python verify.py
```

Expected result: default and round-trip both equal to `Hello, World!`; greeting print and 0. output

The schematic identifier was randomly generated with the high bit set. Control uses the native parser via pycapnp, not a parser built for the corpus.

Recorded status: syntax verified; behavior verified. Toolchain proven: Python 3.13.9 + pycapnp 2.2.4 (native Cap’n Proto parser/runtime ). See [log](verification/verification.log).

Primary sources or original references of the project:

- [Cap’n Proto — linguaggio degli schemi](https://capnproto.org/language.html)
- [pycapnp — lettura e scrittura](https://capnproto.github.io/pycapnp/quickstart.html)

Reproducible dependencies in a dedicated workbook:

```sh
python -m pip install pycapnp==2.2.4
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.capnp` | [hello.capnp](hello.capnp) verified |
