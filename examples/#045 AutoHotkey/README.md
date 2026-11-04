# #045 AutoHotkey

Voce canonica: `AutoHotkey`, tipo `programming`, `language_id: 26`.

Send Hello, World! and LF to the stdout stream and finish AutoHotkey v2.

## Toolchain and reproduction

Official AutoHotkey 64-bit portable interpreter v2, 2.0.27. Test environment: **Windows x64**.

Extract the official package AutoHotkey 2.0.27 and use AutoHotkey64.exe. The code requires v2.0; it is not syntax AutoHotkey v1.

Comando/procedura from the example directory:

```text
AutoHotkey64.exe /ErrorStdOut hello.ahk
```

Exit 0; stdout captured exactly Hello, World! followed by LF.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

FileAppend with destination * writes on stdout. A GUI Windows launcher may not show it directly in the prompt: acquire or redirect stdout, as in the recorded test. No finestra/hotkey comes created.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm)
- [https://www.autohotkey.com/download/2.0/](https://www.autohotkey.com/download/2.0/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ahk` | [hello.ahk](hello.ahk) verified |
| `.ah1` | [hello.ah1](variants/ext-ah1-2e616831/hello.ah1) created; verification pending |
| `.ah2` | [hello.ah2](variants/ext-ah2-2e616832/hello.ah2) created; verification pending |
| `.ahkl` | [hello.ahkl](variants/ext-ahkl-2e61686b6c/hello.ahkl) created; verification pending |
