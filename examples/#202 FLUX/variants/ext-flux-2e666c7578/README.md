# 0202 FLUX: variant `.flux`

Role: Source FLUX UMass in the same .fx format; not InfluxDB Flux language.

Tipo variante: **alias**. Copia byte-identica di examples/#202 FLUX/hello.fx

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
FLUX UMass compiler: generare il C++ da hello.flux e collegare l’implementazione mImpl.cpp del modello in un progetto temporaneo.
```

Expected result: Generazione/compilazione successful; server outputs a Hello, World! line and ends 0.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/emeryberger/flux](https://github.com/emeryberger/flux)
- [https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html](https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/FLUX](https://github.com/github-linguist/linguist/tree/main/samples/FLUX)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
