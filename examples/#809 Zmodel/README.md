# #809 Zmodel

Voce canonica e ordine originali di reference/languages.yml.

Analyze a Zmodel scheme with default greeting.

## Toolchain and reproduction

ZenStack 2.22.3; Prisma 6.19.0; Node.js 22.20.0; Python 3.13.9; SQLite 3.51.0. Test performed on Windows x64.

From the example folder, install isolated dependencies and check:

```text
npm --prefix .tools install --save-exact zenstack@2.22.3 @zenstackhq/runtime@2.22.3; npm --prefix .tools-prisma install --save-exact prisma@6.19.0
python verify.py .tools .tools-prisma
```

## Status and evidence

Artefatto created; syntax verified; behavior verified.

The official ZenStack parser uploads the original scheme and its PrismaSchemaGenerator produces the Prisma scheme. Prisma 6 valid and generates SQL; SQLite inserts a row without message and checks the default greeting. The policy allow is not exercised through a ORM client. Dependencies and results are isolated from the sample folder.

Expected result: Hello, World!.

Log reale: [verification/result.json](verification/result.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Primary sources

- [https://github.com/zenstackhq/zenstack/tree/v2.22.3](https://github.com/zenstackhq/zenstack/tree/v2.22.3)
- [https://zenstack.dev/docs/reference/cli](https://zenstack.dev/docs/reference/cli)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.zmodel` | [hello.zmodel](hello.zmodel) syntax and behavior verified |
