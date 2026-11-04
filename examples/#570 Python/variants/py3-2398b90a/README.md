# 0570: Python: `.py3`

## Latest recorded verification

**Syntax and behavior verified** for `.py3`. CPython console interpreter executes this exact Python variant and captures the greeting. The .pyw check explicitly uses python.exe and does not test Windows GUI file association. [Recorded evidence](../../verification/native_20261104_followup_2e707933.json).

Source Python 3; for .pyw execution GUI normally does not expose a console, while explicit control with python verification stdout.

Origin: copy of the original `examples/#570 Python/hello.py` file.

Artefatto principale: `hello.py3`.

Control provided, from the folder of the variant:

```text
python hello.py3
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)
