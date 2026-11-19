# Verification of 801 main examples on November 19, 2026

This batch recorded one new behavior check. The corpus contains 801 main examples with verified syntax and 801 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_800.md) records the earlier checks in this session.

- **#654 Self**. The upstream Self VM initialized the standard world without graphics and evaluated the unchanged hello.self file. Its printLine message emitted the exact greeting on the VM output stream (captured as stderr), and the VM exited successfully. The same evidence covers `.self`. [Evidence](../examples/%23654%20Self/verification/native_20261119_wave800_main.json).

942 of 1,749 language and extension pairs now have verified behavior.
