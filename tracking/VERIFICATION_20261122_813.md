# Verification of 813 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 813 main examples with verified syntax and 813 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_812.md) for earlier checks.

- **#441 Module Management System**. The offline OpenVMX guest read back the original description. MMK selected HELLO and ran its DCL recipe, which printed the exact line `Hello, World!`. MMK returned VMS condition 1 (SS$_NORMAL). The OpenVMX DCL launcher displayed an abort label and exposed its own failure value %X0000002C in $STATUS. The same evidence covers `.mms`. [Evidence](../examples/%23441%20Module%20Management%20System/verification/native_20261122_wave800_main.json).

951 of 1,749 language and extension pairs now have verified behavior.
