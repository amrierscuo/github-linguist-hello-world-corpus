# Verification of 810 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 810 main examples with verified syntax and 810 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_809.md) for earlier checks.

- **#411 MQL4**. The official MetaEditor compiled the original hello.mq4 into an EX4 file. The official MetaTrader 4 terminal ran the hello script from its startup configuration and recorded the exact `Hello, World!` greeting in the script log. It ran inside an isolated Xvfb display without network access and closed with exit code 0. [Evidence](../examples/%23411%20MQL4/verification/native_20261122_wave800_main.json).

948 of 1,749 language and extension pairs now have verified behavior.
