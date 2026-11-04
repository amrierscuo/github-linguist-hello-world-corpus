# 0513: Ox: `.oxh`

Role: Header Ox with external statement of the Greeting function; separate implementation.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Ox Console/OxMetrics e oxstd. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Ox Console: compilare hello.ox che include hello.oxh
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.ox`: `7376e53d2ed72340807d4a1624eae3d19eb4fc5128a8b367370bbaae6b763c4e`
- `hello.oxh`: `7ef5b8be8dfe030114a21a1b9af0459e6ef1017e197027fb3ef474299a53d201`

Primary sources:

- https://www.doornik.com/ox/
- https://www.doornik.com/ox/ox.html
