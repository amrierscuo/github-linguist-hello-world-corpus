# Verification of 815 main examples on November 23, 2026

This batch recorded one new behavior check. The corpus contains 815 main examples with verified syntax and 815 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_814.md) for earlier checks.

- **#550 PowerBuilder**. The genuine Appeon compiler imported the unchanged u_hello.sru into a local library and built a test application that calls greet(). The matching runtime showed the exact greeting and the function returned 0. The observer read the dialog in a private virtual display and the process exited with code 0. The test application passes the method result to Win32 ExitProcess after writing it to a local result file. The same evidence covers `.sru`. [Evidence](../examples/%23550%20PowerBuilder/verification/native_20261123_wave800_main.json).

953 of 1,749 language and extension pairs now have verified behavior.
