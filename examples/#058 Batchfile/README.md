# #058 Batchfile

Voce canonica: `Batchfile`, tipo `programming`, `language_id: 29`.

Print Hello, World! via the Windows command processor while maintaining the exclamation point.

## Toolchain and reproduction

Windows cmd.exe, Microsoft Windows [Version 10.0.26300.9457 ]. Test environment: **Windows x64**.

Use Windows cmd.exe. The test is performed on Windows 10.0.26300.9457; /d avoids the profile AutoRun instructions.

Comando/procedura from the example directory:

```text
cmd /d /c hello.cmd
```

Exit 0; stdout Hello, World! followed by CRLF.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Setlocal DisableDelayedExpansion keeps literal! even if the caller uses delayed expansion. The log acquires real stdout and converts CRLF to LF via text mode.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://learn.microsoft.com/windows-server/administration/windows-commands/echo](https://learn.microsoft.com/windows-server/administration/windows-commands/echo)
- [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bat` | [hello.bat](variants/ext-bat-2e626174/hello.bat) created; verification pending |
| `.cmd` | [hello.cmd](hello.cmd) verified |
