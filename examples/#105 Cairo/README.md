# #105 Cairo

Fill out and execute a modern Cairo program that prints Hello, World!.

Canonical type: `programming`; `language_id`: `620599567`.

Suggested toolchain: Scarb 2.11.4 with cairo_execute 2.11.4 (project fixed to the version of the guide).

From the example folder, depending on the PATH:

```sh
scarb build
scarb execute
```

Expected result: between Scarb messages, a `Hello, World!` line and 0. output

Cairo modern and Cairo Zero are separate voices of the reference.This project uses the executable and Scarb attribute; it is not a Starknet contract.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Cairo Book — Hello, World](https://www.starknet.io/cairo-book/ch01-02-hello-world.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cairo` | [lib.cairo](src/lib.cairo) created; verification pending |
