# #541 Pod

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze POD and render greeting Hello, World! as documentation.

hello.pod contains POD directives and an original paragraph. The driver uses the original parser/render of the Perl library.

## Toolchain and reproduction

Perl5.38.2, Pod::Simple::Text originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
perl render.pl
```

## Expected result and status

Text rendered contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://perldoc.perl.org/perlpod
- https://perldoc.perl.org/Pod::Simple::Text

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pod` | [hello.pod](hello.pod) verified |
