# 0168 Dockerfile: variant `.dockerfile`

Role: Build file in the Dockerfile language; suffix does not indicate YAML/Quadlet .container.

Tipo variante: **alias**. Copia byte-identica di examples/#168 Dockerfile/Dockerfile

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
docker build -f hello.dockerfile -t corpus-greeting <contesto-temporaneo>; docker run --rm corpus-greeting
```

Expected result: Parser: FROM alpine: 3.22.2 and CMD exec-form correct; runtime predicted stdout Hello, World! more newline, exit 0.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.docker.com/reference/dockerfile/](https://docs.docker.com/reference/dockerfile/)
- [https://github.com/rcjsuen/dockerfile-ast](https://github.com/rcjsuen/dockerfile-ast)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
