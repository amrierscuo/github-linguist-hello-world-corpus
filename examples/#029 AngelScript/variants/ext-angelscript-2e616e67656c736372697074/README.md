# 0029 AngelScript: variant `.angelscript`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#029 AngelScript/hello.as

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
AngelScript host originale: compilare e invocare la funzione del file hello.angelscript con lo stesso engine del modello.
```

Expected result: Compilation bytecode and VM: exit 0; stdout exactly Hello, World! followed by newline.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html)
- [https://github.com/anjo76/angelscript/releases/tag/v2.38.0](https://github.com/anjo76/angelscript/releases/tag/v2.38.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
