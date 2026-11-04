# #666 Slim

Render a Slim template with a greeting paragraph.

Canonical type `markup`, language_id `350`.

Suggested toolchain: Ruby3.2.3 + Slim5.2.2 / Temple0.10.7 / Tilt2.9.0.

From the example directory:

```sh
ruby verify.rb
```

Expected result: HTML exact <p> Hello, World! </p>

The text is rendered by the original engine.

Recorded status: syntax verified; behavior verified. Toolchain: Ruby 3.2.3 + Slim 5.2.2 + Temple 0.10.7 + Tilt 2.9.0. [Log](verification/result.json).

Sources:

- [Slim](https://github.com/slim-template/slim)

Install the dependencies in a separate directory:

```sh
gem install slim -v 5.2.2
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.slim` | [hello.slim](hello.slim) verified |
