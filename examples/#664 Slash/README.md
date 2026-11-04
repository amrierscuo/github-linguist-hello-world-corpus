# #664 Slash

Evaluate a Slash template and make greetings.

Canonical type `programming`, language_id `349`.

Suggested toolchain: Slash CLI SAPI original.

From the example directory:

```sh
slash-cli hello.sl
```

Expected result: stdout Hello, World! and newline.

The template uses the output expression of Slash; Ruby ERB does not verify its engine.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Slash](https://github.com/slash-lang/slash)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sl` | [hello.sl](hello.sl) created; verification pending |
