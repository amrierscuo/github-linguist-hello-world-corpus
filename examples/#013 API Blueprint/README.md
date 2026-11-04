# #013 API Blueprint

`hello.apib` describes a `GET /hello` resource with HTTP 200 response, type
`text/plain` and `Hello, World!` body followed by a return to the head.
of contract API; does not start a HTTP server.

## Toolchain and command

It serves Node.js and the official parser Drafter.js 3.2.0, the JavaScript version
compiled by the parser C++ of API Blueprint. You can install it locally:

```powershell
npm install --prefix .tools --ignore-scripts --no-audit --no-fund drafter.js@3.2.0
node verify.cjs .tools/node_modules/drafter.js
```

`verify.cjs` asks first to Drafter to validate the document without diagnostics,
then verify in its AST method, path, state, type and body of the answer.
It does not implement a parser of the format.

## Verification performed

The syntax and semantics of the **document contract** were verified on Windows with
Drafter.js 3.2.0. Expected result and observed:

```text
Drafter: valid, no warnings
AST: GET /hello -> 200 text/plain; body = Hello, World! + LF
```

Control does not prove a server's behavior: this example does not
contains one. Parser files are in a workbook external to the corpus;
origin, SHA-256 and executed command are recorded in `verification.log`.

## Primary sources

- [API Blueprint: specifica](https://apiblueprint.org/documentation/specification.html)
- [API Blueprint: strumenti di parsing](https://apiblueprint.org/developers.html)
- [Repository ufficiale Drafter.js e API parseSync/validateSync](https://github.com/apiaryio/drafter.js)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.apib` | [hello.apib](hello.apib) verified |
