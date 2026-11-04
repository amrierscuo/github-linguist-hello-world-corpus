# #465 NetLinx

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run the NetLinx startup code that writes Hello, World! on the diagnostic channel0.

PROGRAM_NAME and DEFINE_START define the program. SEND_STRING0 uses a NetLinx expression string with the value of greeting.

## Toolchain and reproduction

AMX NetLinx Studio/compiler e controller o runtime compatibile; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Compilare hello.axs ed eseguire DEFINE_START nel runtime NetLinx.
```

## Expected result and status

Diagnostic channel0 shows Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/runtime AMX unprepared; no controller or connected device.

## Primary sources

- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.axs` | [hello.axs](hello.axs), [driver.axs](variants/axi-f70cf351/driver.axs) created; verification pending |
| `.axi` | [hello.axi](variants/axi-f70cf351/hello.axi) created; verification pending |
