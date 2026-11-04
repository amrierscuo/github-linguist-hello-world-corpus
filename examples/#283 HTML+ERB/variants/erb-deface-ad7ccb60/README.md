# 0283: HTML+ERB: `.erb.deface`

Role: Override Deface with insertion directive and ERB body, in app/overrides. hierarchy

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Ruby3.2.3, ERB della libreria standard. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Deface: collocare hello.html.erb.deface sotto app/overrides/posts/show/ e renderizzare il fixture di vista
```

Expected result: A paragraph added after h1 containing Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `fixture.html.erb`: `9212220934071959eee5b86f08428d18c5f93fdb0b302125e2f217d52c8a5cc3`
- `hello.html.erb.deface`: `59fb850d6330c5e58bdb9593ceb94c7eb09542731a00e8679ec3809764e6457d`

Primary sources:

- https://github.com/spree/deface
- https://docs.ruby-lang.org/en/3.2/ERB.html
