# #160 Dart

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Statically analyze and run a Dart program that prints Hello, World!.

main uses a final variable, string concatenation and print. The toolchain is the official SDK Dart isolated in work; it is not necessary Flutter. The execution uses the VM of the same SDK.

## Toolchain and reproduction

Dart SDK ufficiale 3.13.5 stable, Windows x64

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
dart analyze --fatal-infos hello.dart
dart run hello.dart
```

## Expected result and status

No issues found; stdout esatto Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://dart.dev/tools/dart-analyze
- https://dart.dev/tools/dart-run

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dart` | [hello.dart](hello.dart) verified |
