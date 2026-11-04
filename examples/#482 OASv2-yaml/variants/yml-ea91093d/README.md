# 0482: OASv2-yaml: `.yml`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#482 OASv2-yaml/hello.yaml.

Required toolchain: Node.js v22.20.0; {'@apidevtools/swagger-parser': '13.1.0', 'ajv': '8.20.0'}. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.yml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.yml`: `69f7c1b92a9e78cb976d08dde918a7c3ba0ed18a332456891fd80e7e60c83d9b`
- `package.json`: `02af28fa803a896a950d899f50bbc58f5a37142b119ef825a8882ec7b717774a`
- `verify.cjs`: `0abc61b66cac54cb7966da230a2f0de76d1bbd56a25c9800abba2b223f63db97`

Primary sources:

- https://spec.openapis.org/oas/v2.0.html
- https://apidevtools.com/swagger-parser/
- https://ajv.js.org/
