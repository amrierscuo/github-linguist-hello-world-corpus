# 0289: Haml: `.haml.deface`

Role: Override Deface Haml with commentary directive, not simple template rename.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Haml6.3.0, Temple0.10.7, Tilt2.9.0, Thor1.5.0; Ruby3.2.3. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Deface: collocare hello.html.haml.deface sotto app/overrides/posts/show/ e renderizzare il fixture
```

Expected result: Hello, World! paragraph added after h1

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `fixture.html.erb`: `9212220934071959eee5b86f08428d18c5f93fdb0b302125e2f217d52c8a5cc3`
- `hello.html.haml.deface`: `c8e77a714bc31ceff49c6d69ac7b5459fe2c065a496487c1b0ba84e71cb25940`

Primary sources:

- https://github.com/spree/deface
- https://haml.info/docs/yardoc/file.REFERENCE.html
- https://github.com/haml/haml
- https://rubygems.org/gems/haml/versions/6.3.0
