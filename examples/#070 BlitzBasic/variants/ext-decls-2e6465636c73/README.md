# 0070 BlitzBasic: variant `.decls`

Role: BlitzBasic Userlib Declaration for MessageBoxA Windows; the companion shows greeting.

Type: **adapted**. Starting model: examples/#070 BlitzBasic/hello.bb; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Blitz3D/BlitzPlus 32-bit: aggiungere hello.decls al userlib di un progetto temporaneo; compilare ed eseguire consumer.bb.
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://blitzresearch.itch.io/blitz3d](https://blitzresearch.itch.io/blitz3d)
- [https://github.com/blitz-research/blitz3d](https://github.com/blitz-research/blitz3d)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
