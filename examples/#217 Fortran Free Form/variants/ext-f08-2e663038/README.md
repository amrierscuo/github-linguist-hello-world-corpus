# 0217 Fortran Free Form: variant `.f08`

## Latest recorded verification

**Syntax and behavior verified** for `.f08`. Compiled and ran the exact variant with the declared fixed or free source form; .fpp also used the compiler preprocessor. [Recorded evidence](../../verification/native_20261104_followup_2e663038.json).

Role: Sorgente Fortran free form, distinguished by the heading Fortran fixed form.

Tipo variante: **alias**. Copia byte-identica di examples/#217 Fortran Free Form/hello.f90

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gfortran -x f95 -ffree-form hello.f08 -o <output>/hello; <output>/hello
```

Expected result: Compilazione/run exit 0; exact greeting followed by newline.

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html](https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html)
- [https://gcc.gnu.org/onlinedocs/gfortran/](https://gcc.gnu.org/onlinedocs/gfortran/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
