# #046 AutoIt

Voce canonica: `AutoIt`, tipo `programming`, `language_id: 27`.

Write the greeting concatenate on stdout AutoIt and end with code 0.

## Toolchain and reproduction

Official AutoIt x64 and Au3Check portable, 3.3.18.0. Test environment: **Windows x64**.

Extract AutoIt 3.3.18.0 Portable from the official site; use Au3Check.exe and AutoIt3_x64.exe of the install directory.

Comando/procedura from the example directory:

```text
Au3Check.exe hello.au3; AutoIt3_x64.exe /ErrorStdOut hello.au3
```

Expected result: Au3Check: 0 errors and 0 warning; runtime exit 0; stdout Hello, World! followed by CRLF.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

ConsoleWrite produces the stream stdout; a GUI interpreter does not guarantee its display in the prompt without acquisition. The test really captures that stream and normalizes CRLF through text mode.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm](https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm)
- [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.au3` | [hello.au3](hello.au3) verified |
