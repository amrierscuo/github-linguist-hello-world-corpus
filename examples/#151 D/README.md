# #151 D

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Fill D in BetterC mode and print the greeting via ABI C.

Source D declares greeting with const(char)*, @nogc and nothrow. main and puts use extern(C). BetterC mode excludes dependencies from GC and the full D runtime; the greeting function retains the D mangling. This is a verification of the explicitly stated BetterC subset.

## Toolchain and reproduction

LDC 1.43.0, Linux x86_64 ufficiale; linker GNU su Ubuntu WSL

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
ldc2 -betterC hello.d -of=hello
```

```text
./hello
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://dlang.org/spec/betterc.html
- https://github.com/ldc-developers/ldc/releases/tag/v1.43.0

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.d` | [hello.d](hello.d), [consumer.d](variants/ext-di-2e6469/consumer.d), [greeting.d](variants/ext-di-2e6469/greeting.d) created; verification pending |
| `.di` | [greeting.di](variants/ext-di-2e6469/greeting.di) created; verification pending |
