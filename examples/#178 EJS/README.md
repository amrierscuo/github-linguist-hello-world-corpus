# #178 EJS

Fill out a EJS template and get a HTML Hello, World! title via interpolation escaped.

## Toolchain

Node.js v22.20.0; ejs 7.0.1

## Commands and procedure

npm install; node check.cjs

## Expected result

HTML esattamente <h1>Hello, World!</h1> più newline; <world> viene escaped correttamente.

## Status

syntax and behavior verified.

locals.json provides the data; the template uses <% greeting= %> > The test verifies the EJS engine and escaping, without requiring a surrender in the browser.

Actual verification of 2026-10-08T11:56:13.767905+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://ejs.co/#docs](https://ejs.co/#docs)
- [https://github.com/mde/ejs](https://github.com/mde/ejs)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ejs` | [hello.ejs](hello.ejs) verified |
| `.ect` | [hello.ect](variants/ext-ect-2e656374/hello.ect) created; verification pending |
| `.ejs.t` | [hello.ejs.t](variants/ext-ejs-t-2e656a732e74/hello.ejs.t) syntax and behavior verified |
| `.jst` | [hello.jst](variants/ext-jst-2e6a7374/hello.jst) syntax and behavior verified |

## Additional extension verification

- `.ejs.t`: verified on November 4, 2026. [Evidence](verification/native_20261104_178_variants_result.json).
- `.jst`: verified on November 4, 2026. [Evidence](verification/native_20261104_178_variants_result.json).
