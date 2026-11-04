# #765 WebAssembly

Voce canonica `WebAssembly`, tipo `programming`, language_id `956556503`.

WebAssembly module in text format WAT, with memory containing greetings and exported functions that return its position and length.

## Toolchain and reproduction

wabt / Node.js 22.20.0, 1.0.39. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 and package npm wabt, version in the log. `<prefisso-npm>/node_modules/wabt` must exist; the second argument is an external directory already created, where to write hello.wasm.

Comando/procedura from the directory of the example, unless explicit indications:

```text
node verify.cjs <prefisso-npm> <directory-output-esterna>
```

Expected result: Hello, World! and PASS after compilation, instigation and reading of memory.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

WABT performs parseWat, resolveNames, validated and compiled. Node's native WebAssembly engine instigates bytecode; the driver invokes export and actually reads the memory to get the greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://webassembly.github.io/spec/core/text/modules.html](https://webassembly.github.io/spec/core/text/modules.html)
- [https://github.com/WebAssembly/wabt](https://github.com/WebAssembly/wabt)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.wast` | [hello.wast](variants/wast-39778c33/hello.wast) created; verification pending |
| `.wat` | [hello.wat](hello.wat) verified |
