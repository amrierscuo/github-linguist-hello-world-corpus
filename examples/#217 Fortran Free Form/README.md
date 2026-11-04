# #217 Fortran Free Form

## Latest recorded verification

Latest extension checks:
- `.f03`: Compiled and ran the exact variant with the declared fixed or free source form; .fpp also used the compiler preprocessor. [Evidence](verification/native_20261104_followup_2e663033.json).
- `.f08`: Compiled and ran the exact variant with the declared fixed or free source form; .fpp also used the compiler preprocessor. [Evidence](verification/native_20261104_followup_2e663038.json).
- `.f95`: Compiled and ran the exact variant with the declared fixed or free source form; .fpp also used the compiler preprocessor. [Evidence](verification/native_20261104_followup_2e663935.json).

Voce canonica `Fortran Free Form`, tipo `programming`, language_id `761352333`.

Fill out a Fortran 2008 program in free form and print a parametric concatenation.

## Toolchain and reproduction

GNU Fortran compiler extracted locally from Ubuntu, GNU Fortran (Ubuntu 13.3.0-6ubuntu2 ~ 24.04.1 ) 13.3.0. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU Fortran 13.3.0 on Ubuntu 24.04. implied none, character parameter and free form lines distinguish this source from the fixed-shaped voice.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gfortran -std=f2008 -ffree-form hello.f90 -o build/hello; ./build/hello
```

Expected result: Compilazione/run exit 0; exact greeting followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic compiler is invoked with -ffree-form and -std=f2008.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html](https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html)
- [https://gcc.gnu.org/onlinedocs/gfortran/](https://gcc.gnu.org/onlinedocs/gfortran/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.f90` | [hello.f90](hello.f90) verified |
| `.f03` | [hello.f03](variants/ext-f03-2e663033/hello.f03) syntax and behavior verified |
| `.f08` | [hello.f08](variants/ext-f08-2e663038/hello.f08) syntax and behavior verified |
| `.f95` | [hello.f95](variants/ext-f95-2e663935/hello.f95) syntax and behavior verified |