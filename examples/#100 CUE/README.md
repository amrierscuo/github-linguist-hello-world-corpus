# #100 CUE

Build the greeting from prefix and target with CUE interpolation, unify it with the Hello, World! bond and export the text value.

## Toolchain

cue version v0.17.1

## Commands and procedure

With the official CUE v0.17.1 track:

```sh
cue version
cue vet hello.cue
cue export hello.cue -e greeting --out text
```

prefix and target build interpolated value; the second statement
of greeting binds him to the expected greeting. An incompatible value would
fail the evaluation. The text format only exports greetings.

## Expected result

cue vet exit 0; export exit 0, stdout Hello, World! seguito da newline.

## Status

syntax and behavior verified.

The two greeting statements are constraints that CUE unifies, not an override. The real evaluator checks interpolation and compatibility of the final greeting.

Actual verification of 2026-10-08T11:33:52.311212+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://cuelang.org/docs/reference/spec/](https://cuelang.org/docs/reference/spec/)
- [https://cuelang.org/docs/cmd/cue/export/](https://cuelang.org/docs/cmd/cue/export/)
- [https://github.com/cue-lang/cue/releases/tag/v0.17.1](https://github.com/cue-lang/cue/releases/tag/v0.17.1)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cue` | [hello.cue](hello.cue) verified |
