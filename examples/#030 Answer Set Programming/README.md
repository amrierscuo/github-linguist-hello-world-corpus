# #030 Answer Set Programming

`hello.lp` contains a greeting fact and a `#show` directive that only shows `greeting/1`. For this declaring language the result is the atom in a reply set, not an imperative print.

Prerequisites: Python and the official `clingo==5.8.0` package. The local test used CPython 3.13.9 and wheel Windows x64, installed in the workbook only.

```sh
python -m pip install clingo==5.8.0
python verify.py
```

`verify.py` uses `clingo.Control`, the native parser and grounder, and the solver. It requests all models, verifies satisfiability and exhaustive enumeration, and checks that the full list of shown atoms contains only `greeting("Hello, World!")`. The helper prints `Hello, World!` on its first line and confirms the check on its second line. The semantic check verifies the solver result, beyond the helper's printed output.

Toolchain: **Potassco clingo 5.8.0 Python wheel; CPython 3.13.9 Windows x64**.

Status: **Sintassi e semantica verificate.**

Evidence: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). The log keeps exit code, stdout and stderr; the machine paths are normalized.

Primary sources:

- [Documentazione / sorgente ufficiale 1](https://potassco.org/clingo/)
- [Documentazione / sorgente ufficiale 2](https://github.com/potassco/clingo/releases/tag/v5.8.0)
- [Documentazione / sorgente ufficiale 3](https://github.com/potassco/clingo/blob/v5.8.0/libpyclingo/clingo/control.py)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) verified |
