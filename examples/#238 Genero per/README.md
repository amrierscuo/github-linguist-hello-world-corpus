# #238 Genero per

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill out a Genero form with LABEL static Hello, World!.

hello.per declares a GRID and a static LABEL by item tag, identifier and TEXT. The goal is the content of the form; the file is not a 4GL. program The verification requires compiler form and front-end original.

## Toolchain and reproduction

Genero BDL fglform e front-end compatibile; versioni effettive da registrare

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
fglform hello.per
```

```text
Aprire hello.42f con OPEN WINDOW ... WITH FORM in un programma Genero BDL.
```

## Expected result and status

The form shows the LABEL greeting_label with Hello, World! text.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no native parser/compilatore/runtime performed for this item.

Commitments: Toolchain owner Genero form and front-end not prepared; compilation/rendering pendants.

## Primary sources

- https://4js.com/techdocs/fjs-fgl-manual/fgl-topics/c_fgl_FormSpecFiles_LABEL.html
- https://4js.com/online_documentation/fjs-fgl-manual-html/fgl-topics/c_fgl_FormSpecFiles_GRID.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.per` | [hello.per](hello.per) created; verification pending |
