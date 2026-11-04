# #082 BuildStream

Import hello.txt into a BuildStream artifact and read Hello, World! from the exported artifact.

## Toolchain

BuildStream 2.x, project with min-version 2.0; toolchain not performed and concrete version to record.

## Commands and procedure

From the example folder, which contains project.conf:

```sh
bst --version
bst show hello.bst
bst build hello.bst
bst artifact checkout --directory build-artifact hello.bst
cat build-artifact/hello.txt
```

BuildStream manages its source and artifact cache.
hello.txt file from the project; checkout makes the result verifiable.
Register toolchain and build log before accrediting verification.

## Expected result

Build of import and checkout element without errors; hello.txt in the artifact contains exactly Hello, World! plus newline.

## Status

Syntax and behavioral verification pending.

project.conf provides the context of the project; elements/hello.bst uses the local source and import plugin. A YAML parser does not test a BuildStream build.

Remaining requirements:
- BuildStream and backend cache/sandbox not available: project parsing and build/check-out not executed.

## Primary sources

- [https://docs.buildstream.build/master/tutorial/first-project.html](https://docs.buildstream.build/master/tutorial/first-project.html)
- [https://docs.buildstream.build/2.3/format_project.html](https://docs.buildstream.build/2.3/format_project.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bst` | [hello.bst](elements/hello.bst) created; verification pending |
