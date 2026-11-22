# Verification of 814 main examples on November 22, 2026

This batch recorded one new behavior check. The corpus contains 814 main examples with verified syntax and 814 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_813.md) for earlier checks.

- **#147 Cycript**. The standalone Cycript compiler accepted the original hello.cy and emitted JavaScript. The native runtime ran the original file with JavaScriptCore and the C FFI in an offline WSL sandbox. A copy of the native bridge database declared the libc puts symbol for this standalone build. The invocation returned 0 and printed exactly Hello, World! followed by one newline. The same evidence covers `.cy`. [Evidence](../examples/%23147%20Cycript/verification/native_20261122_wave800_main.json).

952 of 1,749 language and extension pairs now have verified behavior.
