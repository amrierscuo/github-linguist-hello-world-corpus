# #416 Makefile

## Latest recorded verification

Latest extension checks:
- `.mak`: GNU Make parsed the exact variant and executed its hello recipe, emitting exactly Hello, World! plus LF. [Evidence](verification/native_20261105_batch_2e6d616b.json).
- `.make`: GNU Make parsed the exact variant and executed its hello recipe, emitting exactly Hello, World! plus LF. [Evidence](verification/native_20261105_batch_2e6d616b65.json).
- `.makefile`: GNU Make parsed the exact variant and executed its hello recipe, emitting exactly Hello, World! plus LF. [Evidence](verification/native_20261105_batch_2e6d616b6566696c65.json).
- `.mk`: GNU Make parsed the exact variant and executed its hello recipe, emitting exactly Hello, World! plus LF. [Evidence](verification/native_20261105_batch_2e6d6b.json).

Perform a Make recipe that prints greetings.

Canonical type `programming`, language_id `220`.

Suggested toolchain: GNU Make and shell POSIX.

From the example directory:

```sh
make --no-print-directory hello
```

Expected result: stdout Hello, World! and LF, exit 0.

The recipe uses a real tab and suppresses the command echo. It does not produce files outside the folder.

Recorded status: syntax verified; behavior verified. Toolchain: GNU Make on Ubuntu 24.04. [Log](verification/result.json).

Sources:

- [GNU Make — ricette](https://www.gnu.org/software/make/manual/html_node/Recipes.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mak` | [hello.mak](variants/mak-6cee4e0b/hello.mak) syntax and behavior verified |
| `.d` | [hello.d](variants/d-d5992320/hello.d) verified |
| `.make` | [hello.make](variants/make-902d3503/hello.make) syntax and behavior verified |
| `.makefile` | [hello.makefile](variants/makefile-1b7c71d7/hello.makefile) syntax and behavior verified |
| `.mk` | [hello.mk](variants/mk-337c4081/hello.mk) syntax and behavior verified |
| `.mkfile` | [hello.mkfile](variants/mkfile-b5a501aa/hello.mkfile) created; verification pending |
