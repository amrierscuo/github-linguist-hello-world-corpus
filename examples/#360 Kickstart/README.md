# #360 Kickstart

Voce canonica `Kickstart`, tipo `data`, language_id `692635484`.

Analyze Kickstart commands and preserve a post section with greeting as configuration data.

## Toolchain and reproduction

Original Pykickstart Kickstart parser, 3.68; Fedora F42 handler. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pykickstart original 3.68, handler Fedora F42. The helper calls KickstartParser.readKickstart and controls language, timezone, script number and inChroot=False.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m pip install pykickstart==3.68; python verify.py hello.ks
```

Expected result: Accepted commands; post-script printf of the greeting preserved exactly; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The test only uses the parser: it does not start Anaconda, does not installa/partiziona a system and does not run the script post. The declared behavior covers the configuration model and the content of the preserved script.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pykickstart.readthedocs.io/en/latest/pykickstart.html](https://pykickstart.readthedocs.io/en/latest/pykickstart.html)
- [https://pykickstart.readthedocs.io/en/latest/sections.html](https://pykickstart.readthedocs.io/en/latest/sections.html)
- [https://github.com/pykickstart/pykickstart](https://github.com/pykickstart/pykickstart)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ks` | [hello.ks](hello.ks) verified |
