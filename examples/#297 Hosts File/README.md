# #297 Hosts File

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Analyze an Illustrative Hosts File that associates hello-world.example.invalid to 192.0.2.1.

A hostname does not contain spaces or punctuation of greetings: the appropriate equivalent is the hello-world name. The original Hosts parser reads only the explicit path of fixtures; the operating system file is not written or used as a resolver.

## Toolchain and reproduction

python-hosts1.1.3, CPython3.13.9

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

IPv4 voice with indirizzo192.0.2.1 and hello-world.example.invalid name; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://man7.org/linux/man-pages/man5/hosts.5.html
- https://github.com/jonhadfield/python-hosts
- https://www.rfc-editor.org/rfc/rfc6761.html
