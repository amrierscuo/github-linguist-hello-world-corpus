# Verification of 783 main examples on November 19, 2026

This batch recorded 2 new behavior checks. The corpus contains 783 main examples with verified syntax and 783 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_781.md) records the earlier checks in this session.

- **#322 JCL**. The guest executed HELLO with SYSUT2 routed to the configured class Z line printer. The native job boundaries in the changed printer output enclosed the exact greeting. The same evidence covers `.jcl`. [Evidence](../examples/%23322%20JCL/verification/native_20261119_wave800_main.json).
- **#444 Monkey C**. The official compiler built the exact project against the recorded fenix7 profile. The official isolated simulator ran it and emitted the exact greeting. The same evidence covers `.mc`. [Evidence](../examples/%23444%20Monkey%20C/verification/native_20261119_wave800_main.json).

926 of 1,749 language and extension pairs now have verified behavior.
