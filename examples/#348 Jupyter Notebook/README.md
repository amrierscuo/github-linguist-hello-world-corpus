# #348 Jupyter Notebook

Voce canonica `Jupyter Notebook`, tipo `markup`, language_id `185`.

Validate an original notebook and start the real Python kernel to calculate and print the greeting.

## Toolchain and reproduction

Official nbformat, nbclient and genuine Jupyter Python kernel, nbformat 5.10.4; nbclient 0.10.2; ipykernel 7.1.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

nbformat 5.10.4, nbclient 0.10.2 and ipykernel 7.1.0 already present. Requires the kernelspec python3 local. The initial notebook has empty outputs; the completed copy remains in build.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py hello.ipynb build
```

Expected result: valid Notebook; cell performed once; stdout Hello, World!; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il validator autentico controlla la struttura prima e dopo l’esecuzione. Il kernel esegue la cella originale e il controllo confronta execution_count e stream stdout; il log registra l’hash del notebook prodotto. Un warning Windows ZMQ sulla selector thread non impedisce l’esecuzione.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://nbformat.readthedocs.io/en/latest/](https://nbformat.readthedocs.io/en/latest/)
- [https://nbclient.readthedocs.io/en/latest/client.html](https://nbclient.readthedocs.io/en/latest/client.html)
- [https://jupyter.org/](https://jupyter.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ipynb` | [hello.ipynb](hello.ipynb) verified |
