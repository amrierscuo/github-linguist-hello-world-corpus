# #538 Pip Requirements

Voce canonica `Pip Requirements`, tipo `data`, language_id `684385621`.

Solve a Pip requirements list for an original local package that returns greeting.

## Toolchain and reproduction

Actual pip requirements reader/local package resolver and Python, pip 26.1 from <user-home>\ AppData\Roaming\Python\Python313\site-packages\pip (python 3.13 ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pip 26.1 and Python 3.13.9 with setuptools. The test copy requirements and project in work, installs only in the temporary folder and does not use the network.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install --no-index --no-deps --no-build-isolation --target build/installed -r requirements.txt; PYTHONPATH=build/installed python -m corpus_greeting
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real parser/resolver of Pip reads the local requirement, costruisce/install the original package and the installed module prints the greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pip.pypa.io/en/stable/reference/requirements-file-format/](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
