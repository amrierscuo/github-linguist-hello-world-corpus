# #089 CAP CDS

Define in CAP CDS an entity Greeting with field message type String( 13 ), default value Hello, World! and greeting note equal to greeting; fill in CSN and SQL.

## Toolchain

Node.js v22.20.0; @sap/cds-compiler 7.1.1

## Commands and procedure

From this folder:

```sh
npm install
node check.cjs
```

The checker uses compileSync of SAP compiler, reads CSN typed
obtained and generates SQL SQLite with compiler.to.sql.
tipo/lunghezza/default of the field and annotation, then the default in SQL.

## Expected result

Exit 0; CSN solves cds.String, = length 13, default.val = Hello, World!; SQL SQLite contains DEFAULT Hello, World!.

## Status

syntax and behavior verified.

The verified semantics cover the compiled model and SQL generation. No CAP deployment or database execution is claimed.

Actual verification of 2026-10-08T11:33:47.627864+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://cap.cloud.sap/docs/cds/cdl](https://cap.cloud.sap/docs/cds/cdl)
- [https://cap.cloud.sap/docs/cds/csn](https://cap.cloud.sap/docs/cds/csn)
- [https://cap.cloud.sap/docs/cds/compiler/messages](https://cap.cloud.sap/docs/cds/compiler/messages)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cds` | [hello.cds](hello.cds) verified |
