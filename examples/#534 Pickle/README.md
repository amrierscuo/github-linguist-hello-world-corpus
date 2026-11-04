# #534 Pickle

Voce canonica `Pickle`, tipo `data`, language_id `284`.

Read an original Pickle of only data that contains message and language.

## Toolchain and reproduction

Python standard-library Pickle/Pickletools, 3.13.9. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python standard library pickle e pickletools; file originale protocol 4 generato da pickle.dumps.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Genuine disassembly followed by Native Unpickler who refuses any reference to classi/globali. The comparison of the map controls the decoded data.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pkl` | [hello.pkl](hello.pkl) verified |
