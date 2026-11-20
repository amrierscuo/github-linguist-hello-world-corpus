# Verification of 802 main examples on November 20, 2026

This batch recorded one new behavior check. The corpus contains 802 main examples with verified syntax and 802 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261119_801.md) for earlier checks.

- **#757 Volt**. Volta compiled the unchanged bytes of hello.volt with Watt from a temporary src/main.volt copy. The linked x86-64 Linux executable ran in WSL, printed the exact greeting on stdout and exited 0. The same evidence covers `.volt`. [Evidence](../examples/%23757%20Volt/verification/native_20261120_wave800_main.json).

943 of 1,749 language and extension pairs now have verified behavior.
