# #192 Elvish

Run an Elvish script and print Hello, World! followed by LF.

Canonical type `programming`, language_id `570996448`.

Suggested toolchain: Elvish 0.21.0.

From the example directory:

```sh
elvish hello.elv
```

Expected result: exact stdout `Hello, World!\n`, 0. output

echo is a builtin Elvish function. The string is listed and does not expand variables or commands.

Recorded status: syntax verified; behavior verified. Toolchain: Elvish 0.21.0 windows/amd64. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Elvish — tour](https://elv.sh/learn/tour.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.elv` | [hello.elv](hello.elv) verified |
