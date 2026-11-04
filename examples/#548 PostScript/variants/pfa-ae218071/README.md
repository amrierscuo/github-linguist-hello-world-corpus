# 0548: PostScript: `.pfa`

Ruolo: Font PostScript Type 1 ASCII minimo: FullName del saluto e sola glyph .notdef con hsbw/endchar; lenIV -1 disabilita cifratura delle charstring. Non contiene glifi delle lettere del saluto.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Ghostscript10.02.1 ufficiale Ubuntu. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
gs -dSAFER -dBATCH -dNOPAUSE -dNODISPLAY hello.pfa verify.ps
```

Expected result: Defined font and FontInfo.FullName = Hello, World!; empty .notdef renderable.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `hello.pfa`: `c5df05a925489cb214002efc659f79c61ac44fd67f602cac112352a9b9ede971`
- `verify.ps`: `dacf972adb3044ad100fdcd921461423b8d3c2a7013926bb4ee32036e238724f`

Primary sources:

- https://adobe-type-tools.github.io/font-tech-notes/pdfs/T1_SPEC.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf

Additive test actually performed:

Ghostscript defines type1 font, fullName exact Hello, World! and plays show of glyph .notdef; does not claim to glyph textual greetings.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: 10.02.1
