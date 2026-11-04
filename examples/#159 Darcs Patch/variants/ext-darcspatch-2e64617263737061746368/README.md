# 0159 Darcs Patch: variant `.darcspatch`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#159 Darcs Patch/hello.dpatch

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Darcs in repository temporaneo della fixture: darcs apply --dry-run hello.darcspatch; applicare nel repo temporaneo e leggere greeting.txt.
```

Expected result: Application exit 0 and greeting.txt exactly Hello, World! followed by newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://darcs.net/Using/Commands](https://darcs.net/Using/Commands)
- [https://darcs.net/Using/Send](https://darcs.net/Using/Send)
- [https://darcs.net/Binaries](https://darcs.net/Binaries)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
