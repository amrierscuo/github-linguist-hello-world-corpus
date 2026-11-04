# #162 DataWeave

Compose Hello, World! in DataWeave 2 and export a JSON object with greeting.

## Toolchain

Python 3.13.9; DataWeave native 2.12.2 genuine MuleSoft engine binding

## Commands and procedure

python -m pip install -r requirements.txt; python verify.py

## Expected result

Motore senza errori; risultato JSON esattamente {"greeting":"Hello, World!"}.

## Status

syntax and behavior verified.

verify.py uses the official binding Python of the MuleSoft native engine. Greeting comes from the targeting DataWeave concatenation, not from Python.

Actual verification of 2026-10-08T11:56:15.339726+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction](https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction)
- [https://github.com/mulesoft/data-weave-cli](https://github.com/mulesoft/data-weave-cli)
- [https://pypi.org/project/dataweave-native/2.12.2/](https://pypi.org/project/dataweave-native/2.12.2/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dwl` | [hello.dwl](hello.dwl) verified |
