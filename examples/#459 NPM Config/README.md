# #459 NPM Config

Voce canonica `NPM Config`, tipo `data`, language_id `685022663`.

Read the Hello, World! value from the local NPM configuration of the project.

## Toolchain and reproduction

Actual NPM project npmrc parser/config reader, 11.14.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

NPM real 11.14.1. Copy .npmrc in a temporary project with private package.json and use two empty config files to isolate the project.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm --userconfig /path/to/empty-user.npmrc --globalconfig /path/to/empty-global.npmrc config get init-author-name
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The parser/config reader NPM read init-author-name and audit=false. No package installed, no modification to utente/globali. configurations

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.npmjs.com/cli/v11/configuring-npm/npmrc](https://docs.npmjs.com/cli/v11/configuring-npm/npmrc)
- [https://docs.npmjs.com/cli/v11/using-npm/config#init-author-name](https://docs.npmjs.com/cli/v11/using-npm/config#init-author-name)
