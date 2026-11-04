# #697 TL-Verilog

Voce canonica `TL-Verilog`, tipo `programming`, language_id `118656070`.

Translate a TL -Verilog signal that brings the 13 byte ASCII greeting to a SV output.

## Toolchain and reproduction

Required genuine sandpiper-saas compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Request translator TL -Verilog SandPiper/SVGen compatible with TL -X1d and SV simulator.

Comando/procedura from the directory of the example, unless explicit indications:

```text
sandpiper-saas -i hello.tlv -o build/hello.sv; iverilog -g2012 -o build/hello.vvp build/hello.sv; vvp build/hello.vvp
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The TLV block defines the signal and binds it to a wire SV; the greeting is hexadecimal data, so a result display makes the text. Authentic translator not configured; flag pending.

Remaining requirements:

- Required sandpiper-saas toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/TL-X-org/tlv-comp](https://github.com/TL-X-org/tlv-comp)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tlv` | [hello.tlv](hello.tlv) created; verification pending |
