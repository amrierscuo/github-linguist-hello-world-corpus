# #228 GDScript

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run a SceneTree GDScript that builds and prints Hello, World!, then ends.

_initialize is the entry point of SceneTree. The native parser controls the file; the same engine performs the concatenation, print and quit. Headless tests do not require windows or graphical assets.

## Toolchain and reproduction

Godot Engine 4.7.2.stable.official.ed1daf0bf Windows x64

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
godot --headless --path . --check-only --script hello.gd
```

```text
godot --headless --path . --script hello.gd
```

## Expected result and status

The Godot banner is followed by Hello, World! and the process ends exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html
- https://docs.godotengine.org/en/stable/classes/class_scenetree.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gd` | [hello.gd](hello.gd) verified |
