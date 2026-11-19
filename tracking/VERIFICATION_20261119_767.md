# Verification of 767 main examples on November 19, 2026

This batch recorded 6 new behavior checks. The corpus contains 767 main examples with verified syntax and 767 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

The [previous checkpoint](VERIFICATION_20261119_761.md) records the earlier checks in this session.

- **#025 Aleo**. The native snarkVM parsed the unchanged source, evaluated greeting offline and returned a public array whose ASCII decoding is the exact greeting. The same evidence covers `.aleo`. [Evidence](../examples/%23025%20Aleo/verification/native_20261119_wave800_main.json).
- **#059 Beef**. The official CLI built the original Beef source in a minimal console workspace. The native executable printed the exact greeting. The same evidence covers `.bf`. [Evidence](../examples/%23059%20Beef/verification/native_20261119_wave800_main.json).
- **#114 Charity**. The original interpreter evaluated the corrected Charity expression. Its resulting character list is displayed as the exact greeting. The same evidence covers `.ch`. [Evidence](../examples/%23114%20Charity/verification/native_20261119_wave800_main.json).
- **#373 Lambdapi**. The actual proof assistant type-checked and normalized the original greeting. Its resulting list of thirteen natural numbers decodes to the exact ASCII string. The same evidence covers `.lp`. [Evidence](../examples/%23373%20Lambdapi/verification/native_20261119_wave800_main.json).
- **#474 Nit**. The genuine Nit bootstrap generated a standalone compiler. The compiled program ran the interpolation and emitted the greeting. The same evidence covers `.nit`. [Evidence](../examples/%23474%20Nit/verification/native_20261119_wave800_main.json).
- **#626 RouterOS Script**. The vendor RouterOS console parsed and executed the exact script bytes transported as an escaped serial command. Its actual console output contained the greeting. The VM ran with no network interfaces and a disposable disk snapshot. The same evidence covers `.rsc`. [Evidence](../examples/%23626%20RouterOS%20Script/verification/native_20261119_wave800_main.json).

914 of 1,749 language and extension pairs now have verified behavior.
