# #216 Fortran

Voce canonica `Fortran`, tipo `programming`, language_id `107`.

Fill out a fixed Fortran program and write a chained string of thirteen characters.

## Toolchain and reproduction

GNU Fortran compiler extracted locally from Ubuntu, GNU Fortran (Ubuntu 13.3.0-6ubuntu2 ~ 24.04.1 ) 13.3.0. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU Fortran 13.3.0 on Ubuntu 24.04. The test uses the compiler locally extracted, local Fortran libraries and assembler/linker GCC 13. The rows respect the columns of the fixed form.

Comando/procedura from the directory of the example, unless explicit indications:

```text
gfortran -std=legacy -ffixed-form hello.f -o build/hello; ./build/hello
```

Expected result: Compilazione/run exit 0; exact greeting followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The voice Fortran canonical uses here the format fixed form; CHARACTER * 13 and WRITE with A format produce greeting without additional padding.

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
| `.f` | [hello.f](hello.f) verified |
| `.f77` | [hello.f77](variants/ext-f77-2e663737/hello.f77) created; verification pending |
| `.for` | [hello.for](variants/ext-for-2e666f72/hello.for) created; verification pending |
| `.fpp` | [hello.fpp](variants/ext-fpp-2e667070/hello.fpp) created; verification pending |
