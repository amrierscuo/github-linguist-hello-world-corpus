# 0131 ColdFusion: variant `.cfml`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#131 ColdFusion/hello.cfm

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Server CFML isolato: GET /hello.cfml e confrontare il body con il modello.
```

Expected result: HTTP 200; text/plain response containing Hello, World!, without debug output.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.lucee.org/reference/tags/output.html](https://docs.lucee.org/reference/tags/output.html)
- [https://docs.lucee.org/reference/tags/content.html](https://docs.lucee.org/reference/tags/content.html)
- [https://docs.lucee.org/reference/tags/setting.html](https://docs.lucee.org/reference/tags/setting.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
