# Verification of 808 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 808 main examples with verified syntax and 808 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_807.md) for earlier checks.

- **#400 LoomScript**. The pinned LoomScript compiler built Main.loom from the unchanged HelloWorld.ls and the recorded project fixture. The native LoomPlayer ran the resulting assembly in an isolated Xvfb display. HelloWorld.run printed the exact line `Hello, World!`. The application loop was stopped after eight seconds by the test timeout, which returned 124. The log also records unavailable audio and failed connection attempts to the optional localhost asset server. The same evidence covers `.ls`. [Evidence](../examples/%23400%20LoomScript/verification/native_20261122_wave800_main.json).

948 of 1,749 language and extension pairs now have verified behavior.
