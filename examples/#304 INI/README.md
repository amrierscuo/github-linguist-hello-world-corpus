# #304 INI

## Latest recorded verification

Latest extension checks:
- `.cfg`: Unchanged suffix variant; main example status unchanged. [Evidence](verification/native_20261104_followup_2e636667.json).
- `.properties`: Unchanged suffix variant; main example status unchanged. [Evidence](verification/native_20261104_followup_2e70726f70657274696573.json).

Read message in a INI greeting section and recover greeting.

## Toolchain

Python 3.13.9 stdlib configparser

## Commands and procedure

python --version; python verify.py

## Expected result

Post greeting and correct message value; stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

The stdlib parser is real and strict=True; the interpolation is disabled because it does not serve the file. verify.py also controls the name of the section.

Actual verification of 2026-10-08T12:29:57.264907+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ini` | [hello.ini](hello.ini) verified |
| `.cfg` | [hello.cfg](variants/cfg-9b787153/hello.cfg) syntax and behavior verified |
| `.cnf` | [hello.cnf](variants/cnf-a92aaf57/hello.cnf) created; verification pending |
| `.container` | [hello.container](variants/container-f1a82e30/hello.container) created; verification pending |
| `.dof` | [hello.dof](variants/dof-3be3c923/hello.dof) created; verification pending |
| `.frm` | The extension includes legacy view descriptor MySQL and binary table file. No genuine export from a compatible server version does not invent internal metadata such as timestamp, checksum or SQL -mode. |
| `.lektorproject` | [hello.lektorproject](variants/lektorproject-74dbf384/hello.lektorproject) created; verification pending |
| `.mount` | [tmp-corpus-hello.mount](variants/mount-c89a52c2/tmp-corpus-hello.mount) created; verification pending |
| `.network` | [hello.network](variants/network-e59c1258/hello.network) created; verification pending |
| `.prefs` | [hello.prefs](variants/prefs-3d6ae810/hello.prefs) created; verification pending |
| `.pro` | [hello.pro](variants/pro-1d8a87ac/hello.pro) created; verification pending |
| `.properties` | [hello.properties](variants/properties-4792f091/hello.properties) syntax and behavior verified |
| `.service` | [corpus-hello.service](variants/service-a434241b/corpus-hello.service) created; verification pending |
| `.socket` | [corpus-hello.socket](variants/socket-342b56ef/corpus-hello.socket) created; verification pending |
| `.target` | [corpus-hello.target](variants/target-459dc81b/corpus-hello.target) created; verification pending |
| `.timer` | [corpus-hello.timer](variants/timer-fc779652/corpus-hello.timer) created; verification pending |
| `.url` | [hello.url](variants/url-4058ac74/hello.url) created; verification pending |
