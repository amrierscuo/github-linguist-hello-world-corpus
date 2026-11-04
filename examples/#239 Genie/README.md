# #239 Genie

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill Genie through the frontend Vala and run the native program Hello, World!.

init is the entry point Genie; [indent= 4 ] declares the indentation and print adds newline. The actual test uses valac -C with isolated vapes, then GCC with isolated headers GLib and WSL libraries.

## Toolchain and reproduction

Vala/Genie 0.56.16, GNU C 13.3.0 e GLib 2.80.0

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
valac hello.gs -o hello
```

```text
./hello
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://wiki.gnome.org/Projects/Genie
- https://gnome.pages.gitlab.gnome.org/vala/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gs` | [hello.gs](hello.gs) verified |
