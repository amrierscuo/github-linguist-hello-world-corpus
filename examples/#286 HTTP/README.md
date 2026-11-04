# #286 HTTP

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze a real HTTP/1.1 response and transfer Hello, World! via a loopback connection.

hello.http is a wire response with header CRLF, blank line and 13 byte body. A fixture sends it intact via socket on 127.0.0.1; h11 analyzes request and response and controls compares the body. The listener uses an ephemeral port, the socket is closed and the thread is expected.

## Toolchain and reproduction

h11 0.16.0 e CPython3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

h11 accetta HTTP200, Content-Length13 e body Hello, World!; fixture conclusa con CLEANUP.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.rfc-editor.org/rfc/rfc9112.html
- https://h11.readthedocs.io/en/stable/basic-usage.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.http` | [hello.http](hello.http) verified |
