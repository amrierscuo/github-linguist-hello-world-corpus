# #057 Ballerina

Voce canonica: `Ballerina`, tipo `programming`, `language_id: 720859680`.

Concatenare e stampare Hello, World! con io:println in Ballerina.

## Toolchain and reproduction

bal, unavailable / not verified. Test environment: **Windows x64**.

Requires Ballerina Swan Lake distribution with ballerina/io. Local version unavailable and to register before verification.

Comando/procedura from the example directory:

```text
bal version; bal run hello.bal
```

Expected result: successful compilation and execution; stdout Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original source with public main function and local string. It was not compiled or executed since bal is not present.

Remaining requirements:

- bal toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://ballerina.io/learn/by-example/hello-world/](https://ballerina.io/learn/by-example/hello-world/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bal` | [hello.bal](hello.bal) created; verification pending |
