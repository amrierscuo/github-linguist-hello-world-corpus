# #609 Redirect Rules

Voce canonica `Redirect Rules`, tipo `data`, language_id `1020148948`.

Read a Netlify rule that rewrites the hello path on a local file with greeting.

## Toolchain and reproduction

Official Netlify Redirect Parser, 16.1.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser Netlify ufficiale 16.1.1, Node 22.20.0.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools @netlify/redirect-parser@16.1.1; node verify.cjs .tools
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

parseAllRedirects is valid and normalizes _redirects; the helper controls from/to/status and the target data. Scope: parsing and local resolution, without deploy or serving HTTP.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.netlify.com/manage/routing/redirects/overview/](https://docs.netlify.com/manage/routing/redirects/overview/)
