# #416 Makefile

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
| `.mak` | [hello.mak](variants/mak-6cee4e0b/hello.mak) created; verification pending |
| `.d` | [hello.d](variants/d-d5992320/hello.d) verified |
| `.make` | [hello.make](variants/make-902d3503/hello.make) created; verification pending |
| `.makefile` | [hello.makefile](variants/makefile-1b7c71d7/hello.makefile) created; verification pending |
| `.mk` | [hello.mk](variants/mk-337c4081/hello.mk) created; verification pending |
| `.mkfile` | [hello.mkfile](variants/mkfile-b5a501aa/hello.mkfile) created; verification pending |
