# #268 Grammatical Framework

Voce canonica `Grammatical Framework`, tipo `programming`, language_id `137`.

Define a GF grammar with an abstract Hello tree and linearize it in the concrete English syntax.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Grammatical Framework. Greeting.gf declares category Message and manufacturer Hello; GreetingEng.gf uses lincat Str without depending on RGL.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gf -make GreetingEng.gf; gf GreetingEng.gf; nella shell GF: l Hello
```

Expected result: Complete Grammar; Hello returns Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The semantic goal is the linearization of the tree, not a general console program.The GF toolchain is absent.

Remaining requirements:

- GF compiler and interactive grammar runtime are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.grammaticalframework.org/doc/gf-refman.html](https://www.grammaticalframework.org/doc/gf-refman.html)
- [https://www.grammaticalframework.org/doc/gf-shell-reference.html](https://www.grammaticalframework.org/doc/gf-shell-reference.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gf` | [Greeting.gf](Greeting.gf), [GreetingEng.gf](GreetingEng.gf) created; verification pending |
