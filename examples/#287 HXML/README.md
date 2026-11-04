# #287 HXML

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Use HXML to configure the Haxe compiler and run the Hello, World! program.

The HXML file is the main artifact: classpath tax, main class and backend --interp. Hello.hx is the compiled fixture. The Haxe compiler reads the configuration and executes the program through its eval interpreter.

## Toolchain and reproduction

Haxe4.3.3, pacchetto Ubuntu4.3.3-1build2

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
haxe hello.hxml
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://haxe.org/manual/compiler-usage-hxml.html
- https://haxe.org/manual/compiler-usage.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hxml` | [hello.hxml](hello.hxml) verified |
