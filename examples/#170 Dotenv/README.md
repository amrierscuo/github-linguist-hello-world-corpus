# #170 Dotenv

Read GREETING from Dotenv format and populate it in an isolated object.

## Toolchain

Node.js v22.20.0; dotenv 18.0.6

## Commands and procedure

npm install; node check.cjs

## Expected result

Oggetto esattamente {GREETING:"Hello, World!"}; saluto stampato e exit 0.

## Status

syntax and behavior verified.

The .env.example file contains only an illustrative greeting, without credentials. dotenv.parse interprets quotes; populate uses a separate object and does not change the environment of the machine.

Actual verification of 2026-10-08T11:56:13.144812+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://github.com/motdotla/dotenv#usage](https://github.com/motdotla/dotenv#usage)
- [https://github.com/motdotla/dotenv#parse](https://github.com/motdotla/dotenv#parse)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.env` | [hello.env](variants/ext-env-2e656e76/hello.env) created; verification pending |
