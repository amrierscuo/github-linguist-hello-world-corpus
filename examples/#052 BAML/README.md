# #052 BAML

Voce canonica: `BAML`, tipo `programming`, `language_id: 502521509`.

Define in BAML a Hello function with structured response whose field message is bound to the literal Hello, World!.

## Toolchain and reproduction

Official BoundaryML BAML CLI, 0.226.2. Test environment: **Windows x64**.

Install locally @boundaryml/baml@0.226.2. generators.baml fixes the version and output TypeScript; the verification has generated 14 file in an isolated copy under work.

Comando/procedura from the example directory:

```text
npx baml-cli generate --from baml_src; BAML playground: eseguire GreetingForWorld con client configurato.
```

Expected result: Successful TypeScript client generation; waiting model call with message exactly Hello, World! (not performed).

## Status and evidence

Artifact **created**; syntax **verified**; behavioral verification **pending**.

The actual BAML compiler accepted the class, function, prompt, literal type and test. The corpus excludes generated code. No model call was made, and no mock was counted as semantic evidence.

Remaining requirements:

- Model invocation has not been performed; semantic greeting output and credentials remain pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://docs.boundaryml.com/ref/baml-cli/generate](https://docs.boundaryml.com/ref/baml-cli/generate)
- [https://github.com/BoundaryML/baml/blob/canary/fern/03-reference/baml/types.mdx](https://github.com/BoundaryML/baml/blob/canary/fern/03-reference/baml/types.mdx)
- [https://docs.boundaryml.com/ref/baml/test](https://docs.boundaryml.com/ref/baml/test)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.baml` | [generators.baml](baml_src/generators.baml), [hello.baml](baml_src/hello.baml) syntax verified |
