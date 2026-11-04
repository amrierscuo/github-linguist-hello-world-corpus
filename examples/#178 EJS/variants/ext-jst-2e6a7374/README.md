# 0178 EJS: variant `.jst`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Compile and render each original template with ejs.renderFile; assert greeting and escaped input. .ect requires a distinct engine and is not tested. [Evidence](../../verification/native_20261104_178_variants_result.json).

Ruolo: Template EJS/JST nello stesso sottoinsieme di interpolazione <%= greeting %>.

Tipo variante: **alias**. Copia byte-identica di examples/#178 EJS/hello.ejs

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
EJS originale: ejs.renderFile("hello.jst", {greeting:"Hello, World!"}); controllare h1.
```

Expected result: HTML exactly <h1> Hello, World! </h1> more newline; <world> is escaped correctly.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://ejs.co/#docs](https://ejs.co/#docs)
- [https://github.com/mde/ejs](https://github.com/mde/ejs)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
