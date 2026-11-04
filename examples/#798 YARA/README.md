# #798 YARA

## Latest recorded verification

Latest extension checks:
- `.yara`: YARA: compile the original rules, match the exact declared greeting.txt (including its trailing LF), and reject a separate Hello, Moon! fixture. [Evidence](verification/native_20261104_followup_2e79617261.json).

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in YARA and recognize the Hello, World! fixture.

The native motor fills the rule and recognizes the greeting; the negative control Hello, Moon! must not correspond.

## Toolchain and reproduction

YARA/yara-python4.5.4 originali

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

A correspondence CorpusGreeting for Hello, World!, none for Hello, Moon!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://yara.readthedocs.io/en/stable/writingrules.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.yar` | [hello.yar](hello.yar) verified |
| `.yara` | [hello.yara](variants/yara-cc22c747/hello.yara) syntax and behavior verified |