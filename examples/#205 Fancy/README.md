# #205 Fancy

Voce canonica `Fancy`, tipo `programming`, language_id `109`.

Send println to a Fancy string containing greeting.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Requires the original compilatore/runtime Fancy and the compatible VM Rubinius. No manual translation in Ruby is used as proof.

Comando/procedura from the directory of the example, unless explicit indications:

```text
fancy hello.fy
```

Expected result: A Hello, World! line.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The syntax sending messages follows the bakkdoor/fancy. project The runtime is not available.

Remaining requirements:

- Fancy and its required Rubinius VM are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/bakkdoor/fancy](https://github.com/bakkdoor/fancy)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fy` | [hello.fy](hello.fy), [greeting.fy](variants/ext-fancypack-2e66616e63797061636b/greeting.fy) created; verification pending |
| `.fancypack` | [hello.fancypack](variants/ext-fancypack-2e66616e63797061636b/hello.fancypack) created; verification pending |
