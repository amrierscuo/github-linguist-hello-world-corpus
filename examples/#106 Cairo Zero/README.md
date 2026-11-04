# #106 Cairo Zero

Write in the Cairo Zero output a felt that encodes in ASCII big-endian Hello, World!.

Canonical type: `programming`; `language_id`: `891399890`.

Suggested toolchain: cairo-lang 0.14.x (Cairo Zero) in a compatible Python environment.

From the example folder, depending on the PATH:

```sh
mkdir -p build
cairo-compile hello.cairo --output=build/hello.json
cairo-run --program=build/hello.json --layout=plain --print_output
```

Expected result: `5735816763073854918203775149089` numerical output, which decoded as byte big-endian gives `Hello, World!`.

The runtime Zero exposes field cells, not a text console. The short string of 13 byte falls into a felt. This lens is about output and decoding, without cryptographic test generation.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Cairo Zero — serialize_word originale](https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/serialize.cairo)
- [Cairo Zero — segmenti e output](https://docs.cairo-lang.org/cairozero/how_cairo_works/segments.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cairo` | [hello.cairo](hello.cairo) created; verification pending |
