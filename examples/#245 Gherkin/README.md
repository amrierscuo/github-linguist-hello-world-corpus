# #245 Gherkin

Execute a Gherkin scenario that composes greeting to the World recipient.

## Toolchain

Node.js v22.20.0; official Cucumber.js 13.3.0

## Commands and procedure

npm install; npx cucumber-js --require steps.cjs hello.feature

## Expected result

A scenario and three step passed; Then compares exactly Hello, World!.

## Status

syntax and behavior verified.

steps.cjs is the glue required for behavior Gherkin. The original Cucumber runner interprets Given/When/Then and the JSON real report attestes three step passed; no custom parser.

Actual verification of 2026-10-08T12:17:26.464731+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/)
- [https://github.com/cucumber/cucumber-js](https://github.com/cucumber/cucumber-js)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.feature` | [hello.feature](hello.feature) verified |
| `.story` | [hello.story](variants/ext-story-2e73746f7279/hello.story) created; verification pending |
