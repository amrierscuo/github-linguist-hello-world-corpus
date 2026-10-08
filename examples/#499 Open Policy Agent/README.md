# #499 Open Policy Agent

Valutare una regola Rego che costruisce il saluto dall’input.

## Toolchain

Version: 1.21.1
Build Commit: 2a109e54103370d2ef288782ef3cb4c8a37902b2-dirty
Build Timestamp: 2026-09-29T19:10:43Z
Build Hostname: 
Go Version: go1.27.1
Platform: windows/amd64
Rego Version: v1
WebAssembly: available

## Procedura

opa check hello.rego hello_test.rego; opa test .; opa eval --data hello.rego --input input.json --format json data.hello.greeting

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:10:45.460417+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.openpolicyagent.org/docs/policy-language](https://www.openpolicyagent.org/docs/policy-language)
- [https://www.openpolicyagent.org/docs/policy-testing](https://www.openpolicyagent.org/docs/policy-testing)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rego` | [hello.rego](hello.rego), [hello_test.rego](hello_test.rego) verificato |
