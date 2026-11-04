# 0522: POV-Ray SDL: `.inc`

Role: Includes POV -Ray that defines a text object TrueType; separate driver scene.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Original POV-Ray SDL parser and renderer, POV-Ray 3.7.0.10 Ubuntu 3build4. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
povray +Idriver.pov +Ohello.png +W800 +H200 -D
```

Expected result: Text Hello, World! in rendering

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.pov`: `5054100ed69fc2682049fba08a75945c831dbf0f51c596c5eb4c94cfeccfcf2b`
- `hello.inc`: `99a22007af1b9872a88f222929edfb64825787bd4f3ef9c25003fb516a5f6046`

Primary sources:

- https://www.povray.org/documentation/view/3.7.0/290/
- https://www.povray.org/documentation/
