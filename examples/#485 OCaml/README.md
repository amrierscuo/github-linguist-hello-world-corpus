# #485 OCaml

Fill and run OCaml.

## Toolchain

OCaml 4.14.1

## Procedure

ocamlc -o build/hello hello.ml; ocamlrun build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:10:44.031687+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://ocaml.org/manual/5.4/programs.html](https://ocaml.org/manual/5.4/programs.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ml` | [hello.ml](hello.ml), [greeting.ml](variants/mli-2a1ba63b/greeting.ml), [main.ml](variants/mli-2a1ba63b/main.ml), [driver.ml](variants/mly-4acf893e/driver.ml) created; verification pending |
| `.eliom` | [hello.eliom](variants/eliom-eb7291f2/hello.eliom) created; verification pending |
| `.eliomi` | [greeting.eliomi](variants/eliomi-438ad78e/greeting.eliomi) created; verification pending |
| `.ml4` | [hello.ml4](variants/ml4-65957964/hello.ml4) created; verification pending |
| `.mli` | [greeting.mli](variants/mli-2a1ba63b/greeting.mli) created; verification pending |
| `.mll` | [hello.mll](variants/mll-85b0301a/hello.mll) created; verification pending |
| `.mly` | [hello.mly](variants/mly-4acf893e/hello.mly) created; verification pending |
