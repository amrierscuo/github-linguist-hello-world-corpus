# Verification of 805 main examples on November 22, 2026

This batch recorded 2 new behavior checks. The corpus contains 805 main examples with verified syntax and 805 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261120_803.md) for earlier checks.

- **#036 AppleScript**. The native osacompile accepted the original source on macOS. The compiled script ran with osascript and returned exactly `Hello, World!` with exit code 0. The same evidence covers `.applescript`. [Evidence](../examples/%23036%20AppleScript/verification/native_20261122_wave800_main.json).
- **#428 Metal**. The Apple Metal compiler accepted the original shader and metallib linked it. A Swift host dispatched the greeting kernel on a Metal device, waited for completion and printed exactly `Hello, World!` from the 13-byte result buffer. The proof includes the Swift host source. The same evidence covers `.metal`. [Evidence](../examples/%23428%20Metal/verification/native_20261122_wave800_main.json).

945 of 1,749 language and extension pairs now have verified behavior.
