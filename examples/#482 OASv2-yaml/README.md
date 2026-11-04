# #482 OASv2-yaml

## Latest recorded verification

Latest extension checks:
- `.yml`: Swagger Parser validates the OpenAPI 2 specification; Ajv checks the response schema; the loopback HTTP fixture returns the exact greeting and no public listener is opened. [Evidence](verification/native_20261104_followup_2e796d6c.json).

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

Real check 2026-10-08T13:10:39.697436+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://spec.openapis.org/oas/v2.0.html](https://spec.openapis.org/oas/v2.0.html)
- [https://apidevtools.com/swagger-parser/](https://apidevtools.com/swagger-parser/)
- [https://ajv.js.org/](https://ajv.js.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.yaml` | [hello.yaml](hello.yaml) verified |
| `.yml` | [hello.yml](variants/yml-ea91093d/hello.yml) syntax and behavior verified |