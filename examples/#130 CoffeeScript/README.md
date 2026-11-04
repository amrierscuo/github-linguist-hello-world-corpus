# #130 CoffeeScript

Voce canonica: `CoffeeScript`, tipo `programming`, `language_id: 63`.

Interpolate the recipient in a CoffeeScript string, fill in JavaScript and print the greeting with Node.

## Toolchain and reproduction

Official CoffeeScript compiler with Node.js runtime, CoffeeScript version 2.7.0. Test environment: **Windows x64**.

CoffeeScript 2.7.0 and Node.js 22.20.0. Run commands in a work copy: the corpus does not include node_modules or the JavaScript generated.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
npm install --prefix .tools coffeescript@2.7.0; node .tools/node_modules/coffeescript/bin/coffee --compile --output build hello.coffee; node build/hello.js
```

Expected result: Exit 0; runtime exit 0; Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The official CoffeeScript compiler produced the JavaScript from the original .coffee source. Node performed that separate product; no JavaScript equivalent is manually rewritten as proof.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://coffeescript.org/#installation](https://coffeescript.org/#installation)
- [https://coffeescript.org/#strings](https://coffeescript.org/#strings)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.coffee` | [hello.coffee](hello.coffee) verified |
| `._coffee` | [hello._coffee](variants/ext-coffee-2e5f636f66666565/hello._coffee) created; verification pending |
| `.cake` | [hello.cake](variants/ext-cake-2e63616b65/hello.cake) created; verification pending |
| `.cjsx` | [hello.cjsx](variants/ext-cjsx-2e636a7378/hello.cjsx) created; verification pending |
| `.coffee.erb` | [hello.coffee.erb](variants/ext-coffee-erb-2e636f666665652e657262/hello.coffee.erb) created; verification pending |
| `.iced` | [hello.iced](variants/ext-iced-2e69636564/hello.iced) created; verification pending |
