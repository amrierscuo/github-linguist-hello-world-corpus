# 0416: Makefile: `.mkfile`

Role: Plan 9 mk: attribute V of the virtual target; syntax distinct from GNU make.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: GNU Make on Ubuntu 24.04. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
mk -f hello.mkfile all
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.mkfile`: `f671b0ee425f33991f4f8343c6920dd18a62a301bd77e518e37a2f686d7f0c98`

Primary sources:

- https://9p.io/sys/doc/mk.html
- https://www.gnu.org/software/make/manual/html_node/Recipes.html
