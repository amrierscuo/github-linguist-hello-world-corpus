# #366 LFE

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Fill in LFE in BEAM and perform the Hello, World! greeting.

defmodule exports main/0; i:format uses ~s format with a list containing World. The original LFE compiler is built by the authentic Erlang source; BEAM performs the product form.

## Toolchain and reproduction

LFE2.2.2, ErlangOTP25/ERTS13.2.2.5

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
lfec hello.lfe
```

```text
erl -noshell -pa . -eval "hello:main(), halt(0)."
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://lfe.io/learn/
- https://github.com/lfe/lfe/tree/v2.2.2

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lfe` | [hello.lfe](hello.lfe) verified |
