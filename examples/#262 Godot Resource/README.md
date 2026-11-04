# #262 Godot Resource

Voce canonica `Godot Resource`, tipo `data`, language_id `738107771`.

Upload a Godot text scene with a Label node and check its text after inscription.

## Toolchain and reproduction

Official Godot PackedScene loader and engine, 4.7.2.stable.official.ed1daf0bf. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Official 4.7.2 stable Windows x64 Godot. Run in a work copy with project.godot, hello.tscn and verify.gd: Godot can create .godot cache and metadata next to the project.

Comando/procedura from the directory of the example, unless explicit indications:

```text
godot --headless --path . --script verify.gd
```

Expected result: Hello, World! and PASS: genuine PackedScene loader and Label.text.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The test uses the true PackedScene loader and compares Label.text with greeting. The semantic scope is the loading of the scene and the value of the widget allocated; no visual verification of the pixels is declared.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html](https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html)
- [https://docs.godotengine.org/en/stable/classes/class_packedscene.html](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [https://github.com/godotengine/godot/releases](https://github.com/godotengine/godot/releases)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gdnlib` | [hello.gdnlib](variants/ext-gdnlib-2e67646e6c6962/hello.gdnlib) created; verification pending |
| `.gdns` | [hello.gdns](variants/ext-gdns-2e67646e73/hello.gdns) created; verification pending |
| `.tres` | [hello.tres](variants/ext-tres-2e74726573/hello.tres) created; verification pending |
| `.tscn` | [hello.tscn](hello.tscn) verified |
