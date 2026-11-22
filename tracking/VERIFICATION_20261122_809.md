# Verification of 809 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 809 main examples with verified syntax and 809 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_808.md) for earlier checks.

- **#412 MQL5**. MetaEditor compiled the original hello.mq5 into an EX5 file. The official MetaTrader 5 terminal ran the compiled script from its startup configuration and recorded `Hello, World!` in the script log. Compilation and execution used a private virtual display and a network-isolated Wine prefix with Wine Mono disabled. [Evidence](../examples/%23412%20MQL5/verification/native_20261122_wave800_main.json).

948 of 1,749 language and extension pairs now have verified behavior.
