# #279 HOCON

Voce canonica `HOCON`, tipo `data`, language_id `679725279`.

Solve a HOCON replacement and a concatenation to get greeting.

## Toolchain and reproduction

Official Lightbend/Typesafe Config HOCON implementation, 1.4.3. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Typesafe/Lightbend Config 1.4.3 official from Maven Central and JDK 21. Java helper calls ConfigFactory.parseFile (...) .resolve ().

Comando/procedura from the directory of the example, unless explicit indications:

```text
java --class-path .tools/config-1.4.3.jar HoconCheck.java hello.hocon
```

Expected result: Hello, World! and PASS: official HOCON parser, concatenation and substitution resolution.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The message value combines a literal fragment, ${target} and an exclamation point.The authentic parser and resolver produce and verify the final value.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/lightbend/config/blob/main/HOCON.md](https://github.com/lightbend/config/blob/main/HOCON.md)
- [https://github.com/lightbend/config](https://github.com/lightbend/config)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hocon` | [hello.hocon](hello.hocon) verified |
