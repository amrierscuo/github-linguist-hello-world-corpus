# #091 CLIPS

Enter a greeting fact and take exactly a CLIPS rule that prints Hello, World! and withdraws the fact.

## Toolchain

Python 3.13.9; clipspy 1.0.6 / bundled native CLIPS engine

## Commands and procedure

From this folder, with a Python environment equipped with clipspy:

```sh
python -m pip install -r requirements.txt
python verify.py
```

The hello.clp source contains only CLIPS constructs. verify.py loads i
constructs, adds a stdout router, resets and runs and compares the number
of rules executed and the text obtained from the engine.

## Expected result

The hello.clp charging engine, reset inserts the fact, run runs a rule; router receives Hello, World! more newline.

## Status

syntax and behavior verified.

verify.py uses API of CLIPS engine and a router to capture its stdout; it does not reimplement the interpreter. Wrapper clipspy and version are recorded in the log.

Actual verification of 2026-10-08T11:33:18.759353+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://www.clipsrules.net/](https://www.clipsrules.net/)
- [https://clipsrules.net/documentation/v641/apg641.pdf](https://clipsrules.net/documentation/v641/apg641.pdf)
- [https://clipspy.readthedocs.io/en/latest/index.html](https://clipspy.readthedocs.io/en/latest/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.clp` | [hello.clp](hello.clp) verified |
