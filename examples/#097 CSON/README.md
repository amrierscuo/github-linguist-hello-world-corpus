# #097 CSON

Decode the CSON file in an object that contains only greeting= Hello, World!.

## Toolchain

Node.js v22.20.0; cson-parser 4.0.9

## Commands and procedure

From this folder:

```sh
npm install
node check.cjs
```

package.json fixes the version of the parser; check.cjs compares the whole
returned object, including the absence of additional fields.

## Expected result

Parser restituisce esattamente {greeting: "Hello, World!"}; exit 0 e saluto su stdout.

## Status

syntax and behavior verified.

CSON uses CoffeeScript data representation. Checker calls cson-parser and compares the real object; it does not use regex to read values.

Actual verification of 2026-10-08T11:33:44.249893+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://github.com/groupon/cson-parser](https://github.com/groupon/cson-parser)
- [https://github.com/bevry/cson](https://github.com/bevry/cson)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cson` | [hello.cson](hello.cson) verified |
