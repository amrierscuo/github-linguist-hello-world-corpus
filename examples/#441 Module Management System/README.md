# #441 Module Management System

## Verified on November 22, 2026

The offline OpenVMX guest read back the original description. MMK selected HELLO and ran its DCL recipe, which printed the exact line `Hello, World!`. MMK returned VMS condition 1 (SS$_NORMAL). The OpenVMX DCL launcher displayed an abort label and exposed its own failure value %X0000002C in $STATUS.

Run `MMK /DESCRIPTION=SYS$SYSROOT:[SYSMGR]DESCRIP.MMS /RULES_FILE=SYS$SYSROOT:[SYSMGR]CORPUS_RULES.MMS /VERIFY=ALL /LOG HELLO`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

[Earlier evidence](verification/native.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.mms` | [descrip.mms](descrip.mms) Syntax and behavior verified |
| `.mmk` | [hello.mmk](variants/mmk-3528f1de/hello.mmk) created; verification pending |

</details>
