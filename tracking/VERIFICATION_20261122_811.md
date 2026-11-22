# Verification of 811 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 811 main examples with verified syntax and 811 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_810.md) for earlier checks.

- **#376 Lasso**. The native Lasso compiler accepted the original hello.lasso9 and GCC linked the resulting object. The offline executable wrote the greeting Hello, World! on one line followed by two empty lines. The process remained active after the greeting and the harness stopped it after 30 seconds (exit 124). The same evidence covers `.lasso9`. [Evidence](../examples/%23376%20Lasso/verification/native_20261122_wave800_main.json).

949 of 1,749 language and extension pairs now have verified behavior.
