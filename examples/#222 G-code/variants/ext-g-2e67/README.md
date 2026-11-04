# 0222 G-code: variant `.g`

Role: Files of the same G-code dialect: the control remains offline, with the dati/obiettivo of the model.

Tipo variante: **alias**. Copia byte-identica di examples/#222 G-code/hello.gcode

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Parser offline della stessa variante G-code del modello: leggere hello.g e controllare la sequenza di comandi senza inviarli a una macchina.
```

Expected result: The M117 command has the Hello, World! message; it does not contain movement instructions.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://marlinfw.org/docs/gcode/M117.html](https://marlinfw.org/docs/gcode/M117.html)
- [https://github.com/AndyEveritt/GcodeParser](https://github.com/AndyEveritt/GcodeParser)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
