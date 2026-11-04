# #500 OpenAPI Specification v2

Validate the OpenAPI contract and the response of a local HTTP consumer.

## Toolchain

Node.js v22.20.0; {'@apidevtools/swagger-parser': '13.1.0', 'ajv': '8.20.0'}

## Procedure

npm install; node verify.cjs hello.yaml

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The original parser valid and derefens the document; Ajv validates the scheme and rejects a different greeting. HTTP loopback consumes the example of the contract. example.invalid is only metadata; no external service is contacted.

Real check 2026-10-08T13:10:39.703765+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://spec.openapis.org/oas/v2.0.html](https://spec.openapis.org/oas/v2.0.html)
- [https://apidevtools.com/swagger-parser/](https://apidevtools.com/swagger-parser/)
- [https://ajv.js.org/](https://ajv.js.org/)
