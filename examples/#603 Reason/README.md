# #603 Reason

Voce canonica `Reason`, tipo `programming`, language_id `869538413`.

Fill Reason and invoke print_endline from the original program.

## Toolchain and reproduction

Original BuckleScript ReScript/Reason compiler with standard library, BuckleScript 9.0.2 (Using OCaml: 4.06.1+BS ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Frontend Reason di BuckleScript 9.0.2 autentico.

Comando/procedura from the directory of the example, unless explicit indications:

```text
bsc -I /path/to/bs-platform/lib/ocaml -bs-package-name corpus-greeting -bs-package-output commonjs:. -o Hello.cmj Hello.re; node Hello.js
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The frontend .re distinct law syntax Reason with terminators and compile to JS; Node performs the result and prints the exact greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://reasonml.github.io/docs/en/quickstart-javascript](https://reasonml.github.io/docs/en/quickstart-javascript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.re` | [Hello.re](Hello.re), [Hello.re](variants/rei-88fa759e/Hello.re) created; verification pending |
| `.rei` | [Hello.rei](variants/rei-88fa759e/Hello.rei) created; verification pending |
