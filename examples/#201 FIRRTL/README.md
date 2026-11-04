# #201 FIRRTL

Voce canonica `FIRRTL`, tipo `programming`, language_id `906694254`.

Describe a FIRRTL circuit with thirteen ASCII outputs that form greeting and an active printf when reset is low.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Requires CIRCT firtool and a RTL simulator. Provide clock and reset to the module; greeting samples[ 0..12 ] must rebuild the greeting.

Comando/procedura from the directory of the example, unless explicit indications:

```text
firtool hello.fir -o build/hello.sv; simulare il modulo Hello con clock e reset in un testbench RTL
```

Expected result: Filler accepts the circuit; ASCII outputs and printf produce Hello, World! during simulation.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The text is an original circuit, with vector UInt< 8 >[ 13 ] and printf of the FIRRTL language. No compilatore/simulatore is available; the only bytes present in the source are not a proof of execution.

Remaining requirements:

- CIRCT firtool and RTL simulation are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/chipsalliance/firrtl-spec](https://github.com/chipsalliance/firrtl-spec)
- [https://circt.llvm.org/docs/Dialects/FIRRTL/](https://circt.llvm.org/docs/Dialects/FIRRTL/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fir` | [hello.fir](hello.fir) created; verification pending |
