# 0312: Inform 7: `.i7x`

Role: Inform 7 extension with Begins/Ends Here header and reusable phrase.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: inform7 version 10.1.2 'Krypton' (29 August 2022); Inform 6 Inform 6.41 for Linux (22nd July 2022); Frotz 2.54. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Inform 7: installare Corpus Greeting.i7x e compilare il fixture hello.ni; eseguire lo story file
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `Corpus Greeting.i7x`: `89648915fab2d3344e5b8ee081536d9eeb8ace4ebb4cf0a67d383413453373f5`
- `hello.ni`: `54009cbe19bf2aea007a5adc7ef87777d0b00e675e75cebfefb0b3e370b81028`

Primary sources:

- https://ganelson.github.io/inform-website/book/WI_27_1.html
- https://github.com/ganelson/inform/releases/tag/v10.1.2
- https://ganelson.github.io/inform-website/
- https://davidgriffith.gitlab.io/frotz/
