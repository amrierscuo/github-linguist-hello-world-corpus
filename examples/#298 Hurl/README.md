# #298 Hurl

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run a Hurl file that asserts HTTP200 and body Hello, World! on a loopback server.

hello.hurl contains GET request, expected status and body assertion. The original fixture starts an HTTPServer only su127.0.0.1 with ephemeral port; it invokes the real Hurl with --test and --variable port, disables proxy and concludes servers, sockets and threads in finally.

## Toolchain and reproduction

Hurl8.0.1 Windows x64, libcurl8.17.0-DEV; CPython3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

1 file/request riuscito, body esatto Hello, World!, seguito da CLEANUP; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://hurl.dev/docs/asserting-response.html
- https://hurl.dev/docs/running-tests.html
- https://github.com/Orange-OpenSource/hurl/releases/tag/8.0.1

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hurl` | [hello.hurl](hello.hurl) verified |
