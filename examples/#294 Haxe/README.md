# #294 Haxe

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Interpret a Haxe program that uses Sys.println for Hello, World!.

Hello class exposes static main():Void, builds a string and uses IO Sys. Verification passes through parser, typechecker and eval interpreter native Haxe, without transpiler replacement.

## Toolchain and reproduction

Haxe4.3.3, pacchetto Ubuntu4.3.3-1build2

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
haxe -cp . -main Hello --interp
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://haxe.org/manual/introduction-hello-world.html
- https://api.haxe.org/Sys.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hx` | [Hello.hx](Hello.hx), [Main.hx](variants/hxsl-d037293c/Main.hx) created; verification pending |
| `.hxsl` | [GreetingShader.hxsl](variants/hxsl-d037293c/GreetingShader.hxsl) created; verification pending |
