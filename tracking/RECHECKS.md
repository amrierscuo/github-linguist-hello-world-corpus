# Additional checks for earlier entries

8 October 2026: Elixir **0190** and Erlang **0196**, originally created with checks pending, passed native compilation or interpretation and execution. Toolchain: Elixir 1.14.0, Erlang OTP 25 / ERTS 13.2.2.5 from original packages isolated outside the corpus. Both output exactly `Hello, World!` followed by LF. The individual logs record the commands, exit codes and SHA-256 values of the artifacts.

Erlang compilation uses the standard `compile:file` API. The BEAM VM then runs `hello:main/0` and exits. The original Elixir runtime interprets the Elixir script.

The Darcs bundle **0159** was regenerated with local context and an illustrative author, applied to a new temporary repository, and checked again before packaging checkpoint 04.

Saved checkpoint ZIPs are immutable snapshots. The current tracker and later ZIPs include the new evidence. Earlier batch reports describe results as of their original checkpoint.

Further checks on 8 October 2026:

- **0502 OpenCL**: Clang 18.1.3 accepted the kernel in OpenCL C 1.2 mode with `-fsyntax-only`, exit code 0. This was a static check; execution with an OpenCL runtime remained pending at this checkpoint.
- **0542 Pod 6**: Rakudo/MoarVM 2022.12 parsed and rendered the document with `--doc=Text`, producing the greeting in the rendered text, exit code 0.
- **0661 Simple File Verification**: RHash 1.4.3 read the SFV file and verified the `greeting.txt` fixture, CRC32 `B4E89E84`, with `Everything OK`, exit code 0. The check covers the SFV format and content integrity.
- **0668 SmPL**: Coccinelle 1.1.1 applied the semantic patch to the original C source. GCC 13.3.0 compiled the result, and the program printed `Hello, World!` with exit code 0.

The individual folders contain READMEs, commands, sources, versions, output and hashes. The SFV and SmPL source files remained byte-identical to the samples created at earlier checkpoints.

An erroneous `.dist` suffix on a Python library version was corrected in 13 logs. Each version was checked against the `Version` field in the original METADATA, with its recorded SHA-256 verified. The `metadata_correction` field documents the correction. Results, commands, outputs, timestamps and source hashes still describe the actual checks.
