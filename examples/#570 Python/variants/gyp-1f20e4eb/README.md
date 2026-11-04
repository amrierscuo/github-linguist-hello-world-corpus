# 0570: Python: `.gyp`

The GYP configuration uses Python literal syntax and is not arbitrary executable Python code.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.gyp`.

Control provided, from the folder of the variant:

```text
gyp hello.gyp (oppure includere hello.gypi in una configurazione GYP); build in work
```

Expected result: variabile/configurazione original greeting.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://gyp.gsrc.io/docs/InputFormatReference.md](https://gyp.gsrc.io/docs/InputFormatReference.md)
