# Verification of 794 main examples on November 19, 2026

This batch recorded 2 new behavior checks. The corpus contains 794 main examples with verified syntax and 794 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_792.md) records the earlier checks in this session.

- **#181 Earthly**. The native Earthly build ran the unchanged Earthfile. The guest verified and exported the exact 14-byte greeting.txt artifact using the recorded Alpine base image. [Evidence](../examples/%23181%20Earthly/verification/native_20261119_wave800_main.json).
- **#205 Fancy**. The historical Fancy interpreter parsed and executed the exact source and its println call produced the greeting. [Evidence](../examples/%23205%20Fancy/verification/native_20261119_wave800_main.json).

936 of 1,749 language and extension pairs now have verified behavior.
