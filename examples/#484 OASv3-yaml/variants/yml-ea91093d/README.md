# 0484: OASv3-yaml: `.yml`

## Latest recorded verification

**Syntax and behavior verified** for `.yml`. Swagger Parser validates the OpenAPI 3 specification; Ajv checks the response schema; the loopback HTTP fixture returns the exact greeting and no public listener is opened. [Recorded evidence](../../verification/native_20261104_followup_2e796d6c.json).

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#484 OASv3-yaml/hello.yaml.

Required toolchain: Node.js v22.20.0; {'@apidevtools/swagger-parser': '13.1.0', 'ajv': '8.20.0'}. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.yml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World!

Status before this check: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.yml`: `0ceb65289f203fe59ba3967c55a71e92885449bdaec146fc17bfb2ceb80834c0`
- `package.json`: `02af28fa803a896a950d899f50bbc58f5a37142b119ef825a8882ec7b717774a`
- `verify.cjs`: `0abc61b66cac54cb7966da230a2f0de76d1bbd56a25c9800abba2b223f63db97`

Primary sources:

- https://spec.openapis.org/oas/v3.0.3.html
- https://apidevtools.com/swagger-parser/
- https://ajv.js.org/
