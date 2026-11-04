# 0180 Eagle: variant `.brd`

Ruolo: Documento PCB EAGLE XML con board/plain/text su layer tPlace; non schematic rinominato.

Type: **adapted**. Starting model: examples/#180 Eagle/hello.sch; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Validatore EAGLE DTD originale: validare hello.brd; aprire in EAGLE/Fusion Electronics e leggere il testo sul board.
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

- [https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm](https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-ULP-OBJECT-TYPES.htm)
- [https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch](https://github.com/github-linguist/linguist/blob/main/samples/Eagle/Eagle.sch)
- [https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd](https://github.com/drtrigon/eagle/blob/master/doc/eagle.dtd)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://help.autodesk.com/view/EAGLE/ENU/](https://help.autodesk.com/view/EAGLE/ENU/)
