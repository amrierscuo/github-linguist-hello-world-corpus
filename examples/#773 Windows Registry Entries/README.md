# #773 Windows Registry Entries

Voce canonica `Windows Registry Entries`, tipo `data`, language_id `969674868`.

File di importazione Windows Registry originale, con valore Message = `Hello, World!` sotto HKCU\Software\CorpusGreeting.

## Toolchain and reproduction

Windows .reg import parser in disposable Windows registry hive, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

The structure follows the REGEDIT5 format documented by Microsoft. The file only uses ASCII characters. For native verification, a disposable Windows environment or an isolated hive supported by the tool is required.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Solo in una VM Windows usa e getta: reg import hello.reg; reg query HKCU\Software\CorpusGreeting /v Message
```

Expected result: Successful import and Message value equal to Hello, World! in the disposable environment.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The log contains only the probe reg /?; this command does not interpret the source and does not attest syntax or behavior. Import has not been performed on the current register.

Remaining requirements:

- Native import requires a disposable Windows hive; no changes to the current registry performed.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23](https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23)
- [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.reg` | [hello.reg](hello.reg) created; verification pending |
