# #050 B (Formal Method)

Voce canonica: `B (Formal Method)`, tipo `programming`, `language_id: 993355937`.

Define a Classical B machine with constant greeting equal to Hello, World! and hello operation that returns the constant one.

## Toolchain and reproduction

probcli, unavailable / not verified. Test environment: **Windows x64**.

Requires ProB/probcli or ProB2 UI with parser Classical B. The actual version must be recorded when the toolchain will be available.

Comando/procedura from the example directory:

```text
ProB2 UI: aprire HelloWorld.mch, eseguire setup dei constants e l’operazione hello, controllare result = "Hello, World!".
```

Expected result: Charged and typed machine; hello enabled operation and result output exactly Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

This canonical entry is the formal method B. The non-printing machine: the greeting is the symbolic value and the result of the operation. No parser/animatore B was executed in this test.

Remaining requirements:

- probcli toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://prob.hhu.de/w/index.php?title=Summary_of_B_Syntax](https://prob.hhu.de/w/index.php?title=Summary_of_B_Syntax)
- [https://prob.hhu.de/w/index.php?title=ProB_Cli](https://prob.hhu.de/w/index.php?title=ProB_Cli)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mch` | [HelloWorld.mch](HelloWorld.mch) created; verification pending |
