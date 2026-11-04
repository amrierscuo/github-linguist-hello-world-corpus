# #282 HTML+EEX

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Renderizzare HTML+EEx e sostituire audience con World.

EEx.eval_file analyzes the template and performs the expression with binding audience. The maker is original EEx. The test launcher sets ROOTDIR/BINDIR for the isolated ERTS and then performs original erlexec; it does not replace parser or maker.

## Toolchain and reproduction

Elixir1.14.0, Erlang/OTP25 e ERTS13.2.2.5, pacchetti Ubuntu

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
elixir render.exs
```

## Expected result and status

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://hexdocs.pm/eex/EEx.html
- https://elixir-lang.org/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.html.eex` | [hello.html.eex](hello.html.eex) verified |
| `.heex` | [hello.heex](variants/heex-06f63f97/hello.heex) created; verification pending |
| `.leex` | [hello.leex](variants/leex-34ca1cfe/hello.leex) created; verification pending |
