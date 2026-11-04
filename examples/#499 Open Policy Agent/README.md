# #499 Open Policy Agent

Evaluate a Rego rule that builds greeting from input.

## Toolchain

Version: 1.21.1
Build Commit: 2a109e54103370d2ef288782ef3cb4c8a37902b2-dirty
Build Timestamp: 2026-09-29T19:10:43Z
Build Hostname: 
Go Version: go1.27.1
Platform: windows/amd64
Rego Version: v1
WebAssembly: available

## Procedure

opa check hello.rego hello_test.rego; opa test .; opa eval --data hello.rego --input input.json --format json data.hello.greeting

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:10:45.460417+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.openpolicyagent.org/docs/policy-language](https://www.openpolicyagent.org/docs/policy-language)
- [https://www.openpolicyagent.org/docs/policy-testing](https://www.openpolicyagent.org/docs/policy-testing)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rego` | [hello.rego](hello.rego), [hello_test.rego](hello_test.rego) verified |
