# #060 Befunge

Voce canonica: `Befunge`, tipo `programming`, `language_id: 30`.

Enter the thirteen characters of greeting from the Befunge- 93 pile, add LF and stop with @.

## Toolchain and reproduction

Chris Pressey reference Befunge- 93 interpreter, 2.25. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Requires the reference interpreter Befunge- 93 v2.25 by Chris Pressey. Unvaried compilation of the upstream: gcc -O2 -o bef bef.c. Run from the directory of the example with a relative short name; the historical interpreter has limited path buffers.

Comando/procedura from the example directory:

```text
bef -q hello.befunge
```

Exit 0; stdout exactly Hello, World! followed by LF.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

String mode pushes characters in reverse order; thirteen commas pop and print the greeting. 25* produces ASCII 10, the comma writes it, and @ terminates execution. -q disables the interpreter banner. The check used the existing parser and runtime, without a custom interpreter for the corpus.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://github.com/catseye/Befunge-93](https://github.com/catseye/Befunge-93)
- [https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown](https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.befunge` | [hello.befunge](hello.befunge) verified |
| `.bf` | [hello.bf](variants/ext-bf-2e6266/hello.bf) created; verification pending |
