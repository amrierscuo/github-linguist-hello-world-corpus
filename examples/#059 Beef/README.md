# #059 Beef

Voce canonica: `Beef`, tipo `programming`, `language_id: 545626333`.

Fill out a Beef console application and print Hello, World! from Program.Main.

## Toolchain and reproduction

BeefBuild.exe, unavailable / not verified. Test environment: **Windows x64**.

The workspace files must be generated with BeefBuild -new in the work copy; the corpus contains the original source module.

Comando/procedura from the example directory:

```text
In una copia di lavoro: BeefBuild -new; sostituire src/Program.bf con il sorgente fornito; BeefBuild -run
```

Expected result: Workspace compiled without errors; Hello, World! console followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Use the main static and Console.WriteLine function of the Beef library. BeefBuild is not present: no compilation or execution is attested.

Remaining requirements:

- BeefBuild.exe toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://www.beeflang.org/docs/getting-start/](https://www.beeflang.org/docs/getting-start/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bf` | [Program.bf](src/Program.bf) created; verification pending |
