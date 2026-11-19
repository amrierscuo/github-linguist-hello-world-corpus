# Verification of 792 main examples on November 19, 2026

This batch recorded 5 new behavior checks. The corpus contains 792 main examples with verified syntax and 792 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_787.md) records the earlier checks in this session.

- **#003 4D**. Official tool4d executed the finalized 4D method in headless mode. The documented LOG EVENT output channel emitted the exact greeting on standard output. The same evidence covers `.4dm`. [Evidence](../examples/%23003%204D/verification/native_20261119_wave800_main.json).
- **#070 BlitzBasic**. The native compiler accepted the unchanged .bb. Its generated LLVM IR passes the exact greeting constant to bbPrint and then calls bbEnd. [Evidence](../examples/%23070%20BlitzBasic/verification/native_20261119_wave800_main.json).
- **#498 Opal**. For the Ruby-to-JavaScript dialect used by the referenced Linguist sample, Opal compiled the corpus source to JavaScript. The compiled code called the browser alert bridge with the exact greeting, which the headless host captured as text. The same evidence covers `.opal`. [Evidence](../examples/%23498%20Opal/verification/native_20261119_wave800_main.json).
- **#655 ShaderLab**. The headless parser resolved the exact greeting as the display label of the typed _Color material property and verified its default RGBA values. The pass uses an HLSL fragment program whose emitted SPIR-V loads the matching property and writes it to the output. The same evidence covers `.shader`. [Evidence](../examples/%23655%20ShaderLab/verification/native_20261119_wave800_main.json).
- **#697 TL-Verilog**. The upstream compiler lowered the 1a greeting design. The verification adapted its legacy net declaration for Icarus Verilog, which simulated the generated design and emitted the exact greeting. The same evidence covers `.tlv`. [Evidence](../examples/%23697%20TL-Verilog/verification/native_20261119_wave800_main.json).

936 of 1,749 language and extension pairs now have verified behavior.
