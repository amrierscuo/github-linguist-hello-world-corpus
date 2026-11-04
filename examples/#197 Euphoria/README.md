# #197 Euphoria

Perform an Euphoria program that prints Hello, World! followed by LF.

Canonical type `programming`, language_id `880693982`.

Suggested toolchain: OpenEuphoria 4.1.0, interpreter eui.

From the example directory:

```sh
eui hello.ex
```

Expected result: exact stdout `Hello, World!\n`, 0. output

The 1 descriptor is the default Euphoria stdout. The program does not require additional libraries or included.

Recorded status: syntax verified; behavior verified. Toolchain: OpenEuphoria 4.1.0 Linux x64. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [OpenEuphoria — Hello World](https://openeuphoria.org/wiki/view/tutHelloWorld.wc)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.e` | [hello.e](variants/ext-e-2e65/hello.e) created; verification pending |
| `.ex` | [hello.ex](hello.ex) verified |
