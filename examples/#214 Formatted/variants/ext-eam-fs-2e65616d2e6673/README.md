# 0214 Formatted: variant `.eam.fs`

Role: Native dataset EAM /Finnis–Sinclair to a species: embedding array of 13 values encoding greeting; didactic numerical fixtures not calibrated, distinct from the fixed-width .for. record

Type: **adapted**. Starting model: examples/#214 Formatted/hello.for; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Reader EAM/FS originale (LAMMPS pair_style eam/fs o ASE EAM): caricare hello.eam.fs e controllare le 13 tabulazioni embedding contro i code point del saluto.
```

Expected result: Reader accepts header, array F(rho), rho(r) and r*phi(r); 13 samples F encode Hello, World!.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/github-linguist/linguist/tree/main/samples/Formatted](https://github.com/github-linguist/linguist/tree/main/samples/Formatted)
- [https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.lammps.org/pair_eam.html](https://docs.lammps.org/pair_eam.html)
