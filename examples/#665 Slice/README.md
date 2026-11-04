# #665 Slice

Fill out a Slice Ice definition with constant string message.

Canonical type `programming`, language_id `894641667`.

Suggested toolchain: ZeroC Ice slice2cpp and SDK Ice.

From the example directory:

```sh
slice2cpp --output-dir build hello.ice
```

Expected result: accepted and constant definition Greeting::message equal to greeting.

The file defines a constant, no server, proxy or network communications.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Ice Slice](https://docs.zeroc.com/ice/latest/the-slice-language)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ice` | [hello.ice](hello.ice) created; verification pending |
