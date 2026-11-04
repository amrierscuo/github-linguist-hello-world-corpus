# #154 DIGITAL Command Language

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Perform an OpenVMS DCL procedure that concatenates and writes Hello, World!.

The .com file is a DIGITAL Command Language procedure. Each command line begins with $, greeting is a string symbol and WRITE uses SYS $ OUTPUT. The OpenVMS 1 status indicates success; it is not the POSIX error code 1.

## Toolchain and reproduction

VSI OpenVMS con DCL; versione effettiva da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
@HELLO.COM
```

## Expected result and status

SYS $ OUTPUT contains Hello, World! and newline; EXIT 1 is the successful status of OpenVMS.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Commitments: OpenVMS/DCL unavailable; no native interpreter has been performed.

## Primary sources

- https://docs.vmssoftware.com/vsi-openvms-dcl-dictionary-a-m/
- https://docs.vmssoftware.com/vsi-openvms-dcl-dictionary-n-z/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.com` | [hello.com](hello.com) created; verification pending |
