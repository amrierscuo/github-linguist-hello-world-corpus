# #632 SIP

Voce e ordine canonici di `reference/languages.yml`. Sorgente e fixture originali.

## Goal

Generate and compile Python binding for a C function that returns `Hello, World!`, then import the extension and call the function.

`hello.sip` contains the SIP description and the C body. The generated code, the object files and the compiled extension remain in the temporary directory of the test.

## Toolchain and reproduction

Authentic test with SIP 6.17.0, CPython 3.12.3, setuptools 84.0.0 and GCC 13.3.0 on Ubuntu 24.04 WSL2 x86_64.

Copiare `hello.sip`, `pyproject.toml` e `verify_runtime.py` in una directory temporanea. Servono un compilatore C e gli header di sviluppo di Python. Dalla copia dell'esempio, con SIP installato nel Python scelto:

```sh
python -m sipbuild.tools.build --build-dir build --verbose
PYTHONPATH=build/corpus_greeting/build/lib.linux-x86_64-cpython-312 python verify_runtime.py
```

The `PYTHONPATH` path here is the one produced in the CPython 3.12 test on Linux x86_64. For another interpreter or system use the directory containing the `corpus_greeting` module compiled, without copying the track into the corpus.

## Expected result and status

`verify_runtime.py` imports the compiled extension, calls `corpus_greeting.corpus_greeting()`, verify the returned and printed value:

```text
Hello, World!
```

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The generation of wrappers, compilation, linking and import with call C end with exit code 0. The previous one-generation test is kept in [verification/toolchain.json](verification/toolchain.json). The new full test is [verification/runtime.json](verification/runtime.json), with versions, commands, relevant environment, output and SHA-256 of the sources and the effectively imported track.

## Primary sources

- [Direttiva Module](https://python-sip.readthedocs.io/en/latest/directives.html#directive-Module)
- [Strumenti di compilazione SIP](https://python-sip.readthedocs.io/en/stable/command_line_tools.html)
- [Distribuzione SIP 6.17.0](https://pypi.org/project/sip/6.17.0/)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.sip` | [hello.sip](hello.sip) syntax and behavior verified |
