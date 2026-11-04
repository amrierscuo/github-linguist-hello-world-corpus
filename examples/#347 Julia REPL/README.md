# #347 Julia REPL

Voce canonica `Julia REPL`, tipo `programming`, language_id `220689142`.

Record a real Julia REPL session with prompt, assignment value, greeting and exit printing.

## Toolchain and reproduction

Official Julia native runtime and actual terminal REPL, julia version 1.13.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Julia ufficiale 1.13.1 e pywinpty già presente su Windows. Il helper usa un terminale ConPTY senza finestra visibile, TERM=dumb e depot isolata. repl-input.txt contiene i comandi originali; replay.jl è una forma batch ausiliaria dello stesso saluto.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify_repl.py <julia.exe> build; oppure julia --startup-file=no --history-file=no --color=no --banner=no e digitare le righe di repl-input.txt
```

Expected result: Prompt julia>, "World", Hello, World!, prompt exit(); PASS of the true session.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

hello.julia-repl.txt è il transcript catturato realmente, distinto dal normale sorgente Julia. Il log conserva l’output terminale grezzo; il transcript rimuove solo controlli VT/cursore, normalizza CRLF e righe vuote, e omette l’avviso di terminale prima del primo prompt. Il controllo richiede prompt, valore "World", stampa e exit 0.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.julialang.org/en/v1/stdlib/REPL/](https://docs.julialang.org/en/v1/stdlib/REPL/)
- [https://docs.julialang.org/en/v1/manual/command-line-interface/](https://docs.julialang.org/en/v1/manual/command-line-interface/)
- [https://github.com/andfoy/pywinpty](https://github.com/andfoy/pywinpty)
