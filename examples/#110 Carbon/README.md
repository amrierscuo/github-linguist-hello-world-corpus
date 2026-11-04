# #110 Carbon

Define the Run input function of the current Carbon toolchain to print Hello, World!.

Canonical type: `programming`; `language_id`: `55627273`.

Suggested toolchain: Carbon experimental, syntax of the commit df3cf9294397bed0db1ae31aa7c3584dce6a075.

From the example folder, depending on the PATH:

```sh
carbon compile --phase=check hello.carbon
```

Expected result: control of accepted types; with the pipeline execution of the same toolchain, `Hello, World!\n` printing.

The syntax Carbon is experimental and is fixed to the specified commit. The documented command controls the types: it is not exchanged for an execution test; linking and execution remain to be tried.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Carbon — esempio originale fissato a commit](https://github.com/carbon-language/carbon-lang/blob/df3cf9294397bed0db1aae31aa7c3584dce6a075/examples/hello_world.carbon)
- [Carbon — driver](https://github.com/carbon-language/carbon-lang/blob/df3cf9294397bed0db1aae31aa7c3584dce6a075/toolchain/docs/driver.md)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.carbon` | [hello.carbon](hello.carbon) created; verification pending |
