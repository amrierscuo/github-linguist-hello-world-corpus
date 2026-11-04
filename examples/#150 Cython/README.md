# #150 Cython

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Fill out a Cython module with variable cdef str and print its value during import.

The parser/compiler Cython generates C from hello.pyx; a C compiler builds a real CPython extension and Python imports it. In the log compilation GCC uses header Python isolated and performs the .so in WSL. setup.py offers the normal setuptools path to play build with Cyth

## Toolchain and reproduction

Cython 3.3.0; GNU C 13.3.0; CPython 3.12.3 Ubuntu WSL (generazione C su Windows Python 3.13.9)

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
python setup.py build_ext --inplace
```

```text
python -c "import hello"
```

## Expected result and status

stdout esatto Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

## Primary sources

- https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html
- https://github.com/cython/cython

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pyx` | [hello.pyx](hello.pyx), [hello.pyx](variants/ext-pxd-2e707864/hello.pyx), [consumer.pyx](variants/ext-pxi-2e707869/consumer.pyx) created; verification pending |
| `.pxd` | [hello.pxd](variants/ext-pxd-2e707864/hello.pxd) created; verification pending |
| `.pxi` | [hello.pxi](variants/ext-pxi-2e707869/hello.pxi) created; verification pending |
