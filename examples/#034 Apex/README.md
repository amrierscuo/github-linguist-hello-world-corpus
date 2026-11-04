# #034 Apex

Build Hello, World!, control it with System.assertEquals and register it with System.debug in an anonymous Apex block.

## File

- `hello.apex`
- `check.cjs`
- `package.json`

## Toolchain and verification

Node.js v22.20.0; @apexdevtools/apex-parser 5.2.0 (parser comunitario). behavior: Salesforce CLI e org di sviluppo autenticata.

Run the commands in the example folder. `package.json` fixes the parser
Community version 5.2.0. `check.cjs` collects errors of the lexer and the
parser and use the appropriate `anonymousUnit` input for an anonymous block.

```powershell
npm install
node check.cjs
```

To complete the behavior use an authenticated development org, replacing
`ALIAS` with your alias; also record `sf --version` and the log returned.

```powershell
sf apex run --file hello.apex --target-org ALIAS
```

The result of the local parser attests the grammar accepted by toolchain
Community. Type control and `System.assertEquals` will be carried out by
Salesforce platform only in the still pending test.

## Expected result

Local control: zero lexer/parser errors, exit 0. Su Salesforce: assertEquals passes and log USER_DEBUG contains Hello, World!.

## State of the test

syntax verified. behavioral verification pending.

syntax verified from the Community parser ANTLR; this control does not compile Salesforce or Apex asset.

Actual Windows x64 test of 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
The log includes hash SHA-256 of the source, observed versions, commands, exit codes, stdout and stderr.

Remaining requirements:
- Salesforce execution and type checking were not performed. An authenticated developer org and Salesforce CLI are required.

## Primary sources

- [https://github.com/apex-dev-tools/apex-parser](https://github.com/apex-dev-tools/apex-parser)
- [https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html](https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-develop-apex-run-anon.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cls` | [CorpusGreeting.cls](variants/ext-cls-2e636c73/CorpusGreeting.cls) created; verification pending |
| `.apex` | [hello.apex](hello.apex) syntax verified |
| `.trigger` | [hello.trigger](variants/ext-trigger-2e74726967676572/hello.trigger) created; verification pending |
