# 0176 ECL: variant `.eclxml`

Role: Archives ECLXML minimum hand-drawn according to the official consumer EclCC::processXmlFile, which reads Query and Query/@originalFilename. Do not declare an export executed by the compiler; the eclcc test is still pending.

Type: **adapted**. Starting model: examples/#176 ECL/hello.ecl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
eclcc -syntax hello.eclxml; per l’esecuzione compilare/inviare questo archivio a un ambiente HPCC locale di prova e confrontare OUTPUT.
```

Expected result: eclcc reads the archive and accepts the OUTPUT query; HPCC execution produces Hello, World!.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html](https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/OUTPUT.html)
- [https://hpccsystems.com/training/documentation/learning-ecl/](https://hpccsystems.com/training/documentation/learning-ecl/)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.hpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.cpp](https://github.com/hpcc-systems/HPCC-Platform/blob/master/ecl/eclcc/eclcc.cpp)
