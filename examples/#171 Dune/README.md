# #171 Dune

Read a Dune project and build the alias hello that performs echo greeting.

## Toolchain

Dune 3.14.0; OCaml 4.14.1

## Commands and procedure

dune --version; ocamlc -version; dune build --display quiet @hello

## Expected result

Build exit 0; action echo writes Hello, World! more newline.

## Status

syntax and behavior verified.

dune-project is the canonical name recognized by Linguist; dunes contains the support rule. Also a rule only echo requires Dune a real OCaml context. Build and local dependencies remain under work during verification.

Actual verification of 2026-10-08T12:01:45.272622+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://dune.readthedocs.io/en/stable/reference/dune-project/index.html](https://dune.readthedocs.io/en/stable/reference/dune-project/index.html)
- [https://dune.readthedocs.io/en/stable/reference/dune/rule.html](https://dune.readthedocs.io/en/stable/reference/dune/rule.html)
- [https://dune.readthedocs.io/en/stable/reference/actions/echo.html](https://dune.readthedocs.io/en/stable/reference/actions/echo.html)
