# #107 CameLIGO

Interpret the greeting value of a CameLIGO module and get Hello, World!.

Canonical type: `programming`; `language_id`: `829207807`.

Suggested toolchain: LIGO 1.14.2 or a version with CameLIGO and run interpreter.

From the example folder, depending on the PATH:

```sh
ligo run interpret greeting --init-file hello.mligo
```

Expected result: `"Hello, World!"` string value.

The example interprets a module value; does not send Tezos operations and does not require a portfolio.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [LIGO — differenze CameLIGO/OCaml](https://ligolang.org/docs/faq/cameligo-ocaml-syntax-diff/)
- [LIGO — run interpret](https://ligolang.org/docs/1.14.2/manpages/run%20interpret/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mligo` | [hello.mligo](hello.mligo) created; verification pending |
