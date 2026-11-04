# 0345: Jsonnet: `.libsonnet`

Role: Jsonnet Library that exports a string; fixtures import the library.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Official Jsonnet C++ compiler/evaluator, Jsonnet commandline interpreter v0.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
jsonnet driver.jsonnet
```

Expected result: "Hello, World!"

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.jsonnet`: `16baeb51f9d910982b6a0617826211ebc5fbe1a9f6bf1d5c3ab59eae351cb009`
- `hello.libsonnet`: `fcebf6eae7df3c1c619fe5211b1bc1e31da633193024f31687f21d786d03cb8b`

Primary sources:

- https://jsonnet.org/learning/tutorial.html
- https://jsonnet.org/ref/spec.html
