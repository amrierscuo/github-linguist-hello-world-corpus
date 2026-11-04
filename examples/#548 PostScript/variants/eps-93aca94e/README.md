# 0548: PostScript: `.eps`

Role: Encapsulated PostScript with BoundingBox and greeting design, distinct from print on stdout.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Ghostscript10.02.1 ufficiale Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -sOutputFile=hello.png hello.eps
```

Expected result: Text Hello, World! in the image

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.eps`: `954792c93b8c980d3b8afa4f3f50170043e103dff7adc01ffef9363be4b80af7`

Primary sources:

- https://www.adobe.com/content/dam/acom/en/devnet/actionscript/articles/5002.EPSF_Spec.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf
