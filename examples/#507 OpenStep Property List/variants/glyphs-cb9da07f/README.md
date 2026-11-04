# 0507: OpenStep Property List: `.glyphs`

Ruolo: Dati del linguaggio canonico OpenStep Property List; schema progetto Glyphs e font completo non verificati.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Python 3.13.9 + openstep-parser 2.0.3. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Parser originale di OpenStep Property List: leggere hello.glyphs
```

Expected result: OpenStep Dictionary with greeting Hello, World!; no valid Glyphs font promise.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.
- The progetto/font Glyphs schema remains not verified; do not import the fixture as a full font.

SHA-256 of variant files:

- `hello.glyphs`: `8678428ef9ea78cc046fe33a353098e90fdbd7349030c1836559ebcfd5a4bda5`

Primary sources:

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/
- https://github.com/schriftgestalt/GlyphsSDK
- https://github.com/kronenthaler/openstep-parser
