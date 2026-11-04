# #602 Readline Config

Voce canonica `Readline Config`, tipo `data`, language_id `538732839`.

Decode an inputrc that associates an escape sequence with the greeting text.

## Toolchain and reproduction

Authentic GNU Bash Readline inputrc reader/bind macro listing — GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Bash 5.2.21 with GNU Readline; the file contains original editing-mode and macro keybinding.

Comando/procedura from the directory of the example, unless explicit indications:

```text
bash --noprofile --norc -c 'bind -f "$1"; bind -S' bash .inputrc
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Parsing and lookup of the real macro: bind -S shows the Hello, World! value. The verified scope and the configuration reading; the physical pressure of the key is not proved.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File.html](https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File.html)
