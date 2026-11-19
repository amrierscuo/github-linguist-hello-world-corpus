# Verification of 781 main examples on November 19, 2026

This batch recorded 3 new behavior checks. The corpus contains 781 main examples with verified syntax and 781 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_778.md) records the earlier checks in this session.

- **#234 Game Maker Language**. The compatible parser read the declaration and assignment as separate statements. The evaluator resolved the actual parsed variable and concatenation and captured the exact greeting from the parsed show_debug_message call. The same evidence covers `.gml`. [Evidence](../examples/%23234%20Game%20Maker%20Language/verification/native_20261119_wave800_main.json).
- **#314 Inno Setup**. The official compiler accepted the exact source. The independent decoder read the genuine compiled InitializeWizard bytecode and resolved the greeting argument and MsgBox call. [Evidence](../examples/%23314%20Inno%20Setup/verification/native_20261119_wave800_main.json).
- **#394 LiveCode Script**. The published headless LiveCode engine loaded the original script-only stack. Its original handler emitted the exact greeting. The same evidence covers `.livecodescript`. [Evidence](../examples/%23394%20LiveCode%20Script/verification/native_20261119_wave800_main.json).

924 of 1,749 language and extension pairs now have verified behavior.
