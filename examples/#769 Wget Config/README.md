# #769 Wget Config

Voce canonica `Wget Config`, tipo `data`, language_id `668457123`.

Configuration GNU Original Wget setting User-Agent on `Hello, World!`, with timeout and limited number of attempts; a local resource returns the same greeting.

## Toolchain and reproduction

GNU Wget, GNU Wget 1.21.4 built on linux-gnu.. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Linux: GNU Wget 1.21.4 and Python 3.12; start the command in the directory of the example.The driver sets WGETRC on the local .wgetrc, opens a temporary loopback port and closes the server at the end of the test.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python3 verify.py
```

Expected result: Hello, World! response, User-Agent observed Hello, World! and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real wget command reads the config and sends the HTTP request. The server observes the User-Agent value, while the driver also controls the received body. No request to an external host is required.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.gnu.org/software/wget/manual/html_node/Wgetrc-Commands.html](https://www.gnu.org/software/wget/manual/html_node/Wgetrc-Commands.html)
