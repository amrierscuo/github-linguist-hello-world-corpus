# #135 Component Pascal

Voce canonica: `Component Pascal`, tipo `programming`, `language_id: 67`.

Export the Hello.Say command to Component Pascal and write Hello, World! in the BlackBox log.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

This module explicitly chooses that Component Pascal runtime; GPCP console is a different library and is not supposed.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
BlackBox Component Builder: aprire Hello.cp come modulo di una copia di lavoro; compilare il modulo; invocare il comando Hello.Say e controllare il log.
```

Expected result: Filled form; Hello.Say command available; log with Hello, World! and newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Say* is a procedure exported without arguments, which can be used as BlackBox command. StdLog.String and StdLog.Ln are output operations.

Remaining requirements:

- BlackBox Component Builder with StdLog library is unavailable; module compilation/invocation is pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://blackboxframework.org/](https://blackboxframework.org/)
- [https://github.com/BlackBoxCenter/blackbox](https://github.com/BlackBoxCenter/blackbox)
- [https://www.oberon.ch/pdf/CP-Lang.pdf](https://www.oberon.ch/pdf/CP-Lang.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cp` | [Hello.cp](Hello.cp) created; verification pending |
| `.cps` | [hello.cps](variants/ext-cps-2e637073/hello.cps) created; verification pending |
