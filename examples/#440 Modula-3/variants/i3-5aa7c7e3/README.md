# 0440: Modula-3: `.i3`

Ruolo: Interfaccia Modula-3 con PROCEDURE Greet, implementazione e main distinti.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Critical Mass Modula-3 cm3 e libm3. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
cm3 con m3makefile del fixture; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `Greeting.i3`: `bc7eacb2d3e9100448f2f75d63309ba4f067d9860440007273b8d352ba4f2c05`
- `Greeting.m3`: `37760a248cbde0a43c904f2d08d1dec4b265c5e6f318b4fddd8e4ce9de0aae8e`
- `Main.m3`: `bb40e3263566a42aadb7b4f5c05eb633e0e7152e2d12bf552ffb99645d7f5a39`
- `m3makefile`: `b19e7d91dd4cf15d0e3dc3fcc8dfc3d18fc76ed139648ea82e163d167afe337c`

Primary sources:

- https://www.cs.purdue.edu/homes/hosking/m3/reference/complete/m3-defn-complete.pdf
- https://github.com/modula3/cm3
