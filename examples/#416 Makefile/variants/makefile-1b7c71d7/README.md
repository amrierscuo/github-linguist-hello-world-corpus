# 0416: Makefile: `.makefile`

## Latest recorded verification

**Syntax and behavior verified** for `.makefile`. GNU Make parsed the exact variant and executed its hello recipe, emitting exactly Hello, World! plus LF. [Recorded evidence](../../verification/native_20261105_batch_2e6d616b6566696c65.json).

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#416 Makefile/Makefile.

Required toolchain: GNU Make on Ubuntu 24.04. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.makefile; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and LF, exit 0.

Status before this check: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.makefile`: `522f2f7a71537199972884632c2535e8f3e0d2fb4222a5e952528af1c0037c57`

Primary sources:

- https://www.gnu.org/software/make/manual/html_node/Recipes.html
