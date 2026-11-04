# #446 MoonBit

Voce canonica `MoonBit`, tipo `programming`, language_id `181453007`.

Fill out an original MoonBit project and print the greeting in the JavaScript target.

## Toolchain and reproduction

Official MoonBit compiler/build tool and core standard library, moon 0.1.20260920 ( 914d7da 2026-09-20 );; Feature flags enabled: rr_moon_mod,rr_moon_pkg. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Official MoonBit and core standard library: Windows portabile distribution, MOON_HOME local. The preparation of the core uses moon bundle --target js --all from the directory lib/core.

Comando/procedura from the directory of the example, unless explicit indications:

```text
moon run --target js cmd/main
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Compiler and build tool authentic accept the project and target JS produces the exact text.The old JSON configuration is still accepted with deprecation notice.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.moonbitlang.com/download](https://www.moonbitlang.com/download)
- [https://docs.moonbitlang.com/en/latest/tutorial/index.html](https://docs.moonbitlang.com/en/latest/tutorial/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mbt` | [main.mbt](cmd/main/main.mbt) verified |
