# Verification of 807 main examples on November 22, 2026

This batch recorded 2 new behavior checks. The corpus contains 807 main examples with verified syntax and 807 with verified behavior, out of 836.

Tools ran from the terminal or in isolated headless environments. This batch used no .NET or Mono toolchain. Open a record for the exact inputs, toolchain, observed results and verification scope.

See the [previous checkpoint](VERIFICATION_20261122_805.md) for earlier checks.

- **#154 DIGITAL Command Language**. The OpenVMX DCL interpreter, built from the pinned upstream source, executed the original command procedure through standard input. The assignment concatenated the two strings, WRITE SYS$OUTPUT printed exactly `Hello, World!`, and the process returned the DCL success status 1 specified by EXIT 1. The same evidence covers `.com`. [Evidence](../examples/%23154%20DIGITAL%20Command%20Language/verification/native_20261122_wave800_main.json).
- **#783 XC**. The official XMOS XC compiler compiled the original .xc source and linked an xCORE executable. The XMOS xsim simulator ran that executable offline and printed exactly `Hello, World!` with exit code 0. The same evidence covers `.xc`. [Evidence](../examples/%23783%20XC/verification/native_20261122_wave800_main.json).

947 of 1,749 language and extension pairs now have verified behavior.
