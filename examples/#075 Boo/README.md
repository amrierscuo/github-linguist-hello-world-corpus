# #075 Boo

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Run a concatenation and print in Boo.

The source uses the original Boo syntax and the inference of the string type. It is not converted into Python; the verification requires authentic booi.

## Toolchain and reproduction

Boo con booi e runtime .NET/Mono compatibile; versione effettiva da registrare

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
booi hello.boo
```

## Expected result and status

stdout Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; no native parser or runtime has been performed for this item.

Commitments: Boo/booi and its compatible runtime not available; no Boo compiler has been executed.

## Primary sources

- https://github.com/boo-lang/boo
- https://boo-language.github.io/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.boo` | [hello.boo](hello.boo) created; verification pending |
