# Verification of 803 main examples on November 20, 2026

This batch recorded one new behavior check. The corpus contains 803 main examples with verified syntax and 803 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261120_802.md) for earlier checks.

- **#513 Ox**. The published Ox compiler and runtime loaded their packaged standard library, compiled the original hello.ox and ran its main function. The worker emitted the exact greeting and reported exit code 0 in a headless WSL process. [Evidence](../examples/%23513%20Ox/verification/native_20261120_wave800_main.json).

943 of 1,749 language and extension pairs now have verified behavior.
