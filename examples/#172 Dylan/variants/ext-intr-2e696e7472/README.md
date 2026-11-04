# 0172 Dylan: variant `.intr`

Role: Melange Dylan interface that imports a function from a header C. Original text form based on the Basic Use section of Melange documentation; the companion C implements the greeting.

Type: **adapted**. Starting model: examples/#172 Dylan/hello.dylan; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
melange hello.intr <output>/hello.dylan; cc -c greeting.c -o <output>/greeting.o; compilare i binding generati e collegare l’oggetto nel progetto Dylan/Mindy compatibile; invocare il binding della funzione hello_world.
```

Expected result: Melange generates bindings for hello_world; the connected consumer Dylan invokes the C function and Hello, World! print.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://opendylan.org/getting-started-cli/hello-world.html](https://opendylan.org/getting-started-cli/hello-world.html)
- [https://opendylan.org/library-reference/io/format-out.html](https://opendylan.org/library-reference/io/format-out.html)
- [https://opendylan.org/download/index.html](https://opendylan.org/download/index.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.cs.cmu.edu/~gwydion/dylan-release/docs/omaker-out/melange.htm](https://www.cs.cmu.edu/~gwydion/dylan-release/docs/omaker-out/melange.htm)
- [https://package.opendylan.org/melange/introduction.html](https://package.opendylan.org/melange/introduction.html)
