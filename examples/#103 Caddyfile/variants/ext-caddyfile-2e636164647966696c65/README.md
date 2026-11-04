# 0103 Caddyfile: variant `.caddyfile`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#103 Caddyfile/Caddyfile

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
caddy adapt --config hello.caddyfile --adapter caddyfile --validate
```

Expected result: GET http://127.0.0.1:18763/ returns state 200 and 13 byte Hello, World!.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://caddyserver.com/docs/caddyfile/directives/respond](https://caddyserver.com/docs/caddyfile/directives/respond)
- [https://caddyserver.com/docs/command-line](https://caddyserver.com/docs/command-line)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
