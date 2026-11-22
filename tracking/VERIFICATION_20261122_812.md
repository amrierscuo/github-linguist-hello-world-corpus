# Verification of 812 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 812 main examples with verified syntax and 812 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_811.md) for earlier checks.

- **#497 Opa**. The native Opa compiler accepted the original hello.opa. The generated JavaScript ran with the Opa runtime in a private network namespace. A loopback HTTP request returned status 200 and the page contained an h1 element whose exact text was Hello, World! The same evidence covers `.opa`. [Evidence](../examples/%23497%20Opa/verification/native_20261122_wave800_main.json).

950 of 1,749 language and extension pairs now have verified behavior.
