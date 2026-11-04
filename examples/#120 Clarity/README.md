# #120 Clarity

Analyze a Clarity contract and call locally greeting, getting the string ASCII Hello, World!.

Canonical type: `programming`; `language_id`: `91493841`.

Suggested toolchain: Clarinet or @stacks/clarinet-sdk with Clarity simulator. The version actually tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
node verify.cjs
```

Expected result: Clarity value (string-ascii 13) equal to `Hello, World!`, without state modifications.

The contract exposes a read-only function; the verification uses only a local simulator and does not publish a contract on Stacks.

Recorded status: syntax verified; behavior verified. Tried toolchain: Node.js 22.20.0 + @stacks/clarinet-sdk 3.24.1 + @stacks/transactions 7.6.0. See [log](verification/verification.log).

Primary sources or original references of the project:

- [Clarity — define-read-only](https://docs.stacks.co/reference/clarity)
- [Clarinet SDK — deployContract e callReadOnlyFn](https://docs.stacks.co/reference/clarinet-js-sdk/sdk-reference)

Automatic verification included: `node verify.cjs`.

Reproducible dependencies in a dedicated workbook:

```sh
npm install --ignore-scripts --no-audit --no-fund @stacks/clarinet-sdk@3.24.1 @stacks/transactions@7.6.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.clar` | [hello.clar](hello.clar) verified |
