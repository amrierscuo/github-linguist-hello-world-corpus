# 0570: Python: `.pyw`

## Latest recorded verification

**Syntax and behavior verified** for `.pyw`. CPython console interpreter executes this exact Python variant and captures the greeting. The .pyw check explicitly uses python.exe and does not test Windows GUI file association. [Recorded evidence](../../verification/native_20261104_followup_2e707977.json).

Source Python 3; for .pyw execution GUI normally does not expose a console, while explicit control with python verification stdout.

Origin: copy of the original `examples/#570 Python/hello.py` file.

Artefatto principale: `hello.pyw`.

Control provided, from the folder of the variant:

```text
python hello.pyw
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)
