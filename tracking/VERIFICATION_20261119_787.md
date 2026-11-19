# Verification of 787 main examples on November 19, 2026

This batch recorded 4 new behavior checks. The corpus contains 787 main examples with verified syntax and 787 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_783.md) records the earlier checks in this session.

- **#340 JetBrains MPS**. The original project descriptors loaded the MPS language, solution and models. The publisher headless generator emitted Java for the source solution. Compiling and running that Java printed the exact greeting. The same evidence covers `.mps`, `.mpl`, `.msd`. [Evidence](../examples/%23340%20JetBrains%20MPS/verification/native_20261119_wave800_main.json).
- **#593 RPGLE**. The compatible RPGLE interpreter loaded the complete source. Its DSPLY sink emitted the exact greeting. The same evidence covers `.rpgle`. [Evidence](../examples/%23593%20RPGLE/verification/native_20261119_wave800_main.json).
- **#629 SAS**. Upstream StatLang expanded a SAS macro variable and its %PUT statement emitted the exact greeting. This proof covers the SAS macro subset used by the finalized code. The same evidence covers `.sas`. [Evidence](../examples/%23629%20SAS/verification/native_20261119_wave800_main.json).
- **#821 mIRC Script**. The upstream headless engine loaded the unchanged .mrc as a script, ran its hello alias, and returned the exact echo text to the batch harness. The same evidence covers `.mrc`. [Evidence](../examples/%23821%20mIRC%20Script/verification/native_20261119_wave800_main.json).

932 of 1,749 language and extension pairs now have verified behavior.
