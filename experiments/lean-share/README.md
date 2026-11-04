# Lean share experiment

This additional sample tests how the Languages bar changes when the amount of Lean source increases. The requested target was at least 5% Lean.

The Lean 4 file contains numbered elementary proofs and a main function that prints Hello, World!. The repetitions are intentional: the Languages share measures source bytes and does not measure functionality or project complexity.

The original 836-entry corpus and its checks are unchanged. The corpus counters exclude this experiment.

GitHub baseline: 569 languages, 259622 total bytes and 375 Lean bytes. After the push, the GitHub Languages API measured **13966 Lean bytes out of 273213 bytes**, or **5.11176%**. The detected language count remained **569**; only the Lean byte count changed. The [full result](verification/github_languages.json) records the commit and measurement time.

Verified with Lean 4.0.0: `lean LeanShare.lean` exits with code 0; `lean --run LeanShare.lean` exits with code 0 and prints `Hello, World!`. The [recorded evidence](verification/lean4.json) includes the version, output and source SHA-256.
