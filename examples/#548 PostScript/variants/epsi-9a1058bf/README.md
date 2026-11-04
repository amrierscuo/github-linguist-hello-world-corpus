# 0548: PostScript: `.epsi`

Role: EPS with section preview ASCII 1-bit conform EPSI; minimum white illustrative preview, greeting in vector content.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Ghostscript10.02.1 ufficiale Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Ghostscript: renderizzare hello.epsi; tool EPSI originale per leggere BeginPreview
```

Expected result: Text Hello, World! in vector rendering; white preview of 8x1 pixel

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.epsi`: `ebd943bd51b0df143b46be7735743e0364899ca4513c16f89567df05f8adbe80`

Primary sources:

- https://www.adobe.com/content/dam/acom/en/devnet/actionscript/articles/5002.EPSF_Spec.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf
