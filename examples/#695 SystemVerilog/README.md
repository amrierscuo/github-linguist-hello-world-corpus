# #695 SystemVerilog

Voce canonica `SystemVerilog`, tipo `programming`, language_id `363`.

Fill and simulate a SystemVerilog2012 testbench that prints greetings.

## Toolchain and reproduction

Authentic Icarus SystemVerilog compiler and vvp simulator, Icarus 12.0-2build2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Icarus Verilog12.0 authentic, frontend selected with -g2012; relocated tool uses -B for native components.

Comando/procedura from the directory of the example, unless explicit indications:

```text
iverilog -g2012 -o build/hello.vvp hello.sv; vvp build/hello.vvp
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Compiler e simulator genuini eseguono string, display e finish; prima riga stdout esatta.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://steveicarus.github.io/iverilog/usage/command_line_flags.html](https://steveicarus.github.io/iverilog/usage/command_line_flags.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sv` | [hello.sv](hello.sv), [main.sv](variants/svh-80e139de/main.sv), [main.sv](variants/vh-02180d63/main.sv) created; verification pending |
| `.svh` | [hello.svh](variants/svh-80e139de/hello.svh) created; verification pending |
| `.vh` | [hello.vh](variants/vh-02180d63/hello.vh) created; verification pending |
