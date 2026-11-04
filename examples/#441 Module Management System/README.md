# #441 Module Management System

Voce canonica `Module Management System`, tipo `programming`, language_id `235`.

Invoke WRITE SYS $ OUTPUT from an OpenVMS Module Management System target.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires OpenVMS and VSI MMS or MMK compatible, with DCL.

Comando/procedura from the directory of the example, unless explicit indications:

```text
MMS /DESCRIPTION=descrip.mms HELLO
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Target and action DCL original; no OpenVMS environment available.

Remaining requirements:

- OpenVMS with MMS/MMK is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.vmssoftware.com/docs/vsi-decset-for-openvms-guide-to-the-module-management-system.pdf](https://docs.vmssoftware.com/docs/vsi-decset-for-openvms-guide-to-the-module-management-system.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mms` | [descrip.mms](descrip.mms) created; verification pending |
| `.mmk` | [hello.mmk](variants/mmk-3528f1de/hello.mmk) created; verification pending |
