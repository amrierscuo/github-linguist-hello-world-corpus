# #051 B4X

Voce canonica: `B4X`, tipo `programming`, `language_id: 96642275`.

Print Hello, World! in the log of a B4J console application without a UI, a variant in the B4X family.

## Toolchain and reproduction

B4J.exe, unavailable / not verified. Test environment: **Windows x64**.

Requires B4J and a compatible JDK. Add Main.bas as the source module of a new non-UI project. The IDE creates the project attributes and metadata.

Comando/procedura from the example directory:

```text
B4J IDE: File > New > Non-UI Project; sostituire il modulo Main con Main.bas; Run in Release; controllare il log.
```

Expected result: Successful Build and a Hello, World! row in the application log.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Uses AppStart(Args() As String) for the B4J console entry point and Log for the greeting. B4J is unavailable, so the module has not been compiled. No complete B4A/B4i project is claimed.

Remaining requirements:

- B4J.exe toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://www.b4x.com/guides/B4XGettingStarted.html](https://www.b4x.com/guides/B4XGettingStarted.html)
- [https://www.b4x.com/android/forum/threads/console-application-output-shown-after-command-prompt.167324/](https://www.b4x.com/android/forum/threads/console-application-output-shown-after-command-prompt.167324/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bas` | [Main.bas](Main.bas) created; verification pending |
