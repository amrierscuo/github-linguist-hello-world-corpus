# 0016 ASN.1: variant `.asn1`

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#016 ASN.1/hello.asn

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
asn1tools compile -c uper hello.asn1; applicare lo stesso test encode/decode del modello al file variante.
```

Expected result: DER 0c0b48656c6c6f20576f726c64; decoded value Hello World; PASS.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://asn1tools.readthedocs.io/en/latest/](https://asn1tools.readthedocs.io/en/latest/)
- [https://github.com/eerimoq/asn1tools](https://github.com/eerimoq/asn1tools)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
