# #570 Python

## Latest recorded verification

Latest extension checks:
- `.cgi`: CPython executes the exact CGI source; validates serialized Content-Type header and body, without starting a CGI server. The driver preserves the source CRLF delimiters on Windows. [Evidence](verification/native_20261104_followup_2e636769.json).
- `.py3`: CPython console interpreter executes this exact Python variant and captures the greeting. The .pyw check explicitly uses python.exe and does not test Windows GUI file association. [Evidence](verification/native_20261104_followup_2e707933.json).
- `.pyw`: CPython console interpreter executes this exact Python variant and captures the greeting. The .pyw check explicitly uses python.exe and does not test Windows GUI file association. [Evidence](verification/native_20261104_followup_2e707977.json).
- `.wsgi`: Standard-library WSGI validator and wsgiref reference handler execute the exact module, asserting its HTTP status, Content-Type, Content-Length and response bytes; in-memory transport. [Evidence](verification/native_20261104_followup_2e77736769.json).

Perform a Python function that builds greeting.

## Toolchain

CPython Python 3.13.9

## Procedure

python hello.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:16:51.063653+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://docs.python.org/3/tutorial/inputoutput.html](https://docs.python.org/3/tutorial/inputoutput.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.py` | [hello.py](hello.py), [greet.py](variants/gyp-1f20e4eb/greet.py), [hello.py](variants/pyi-974aaf0c/hello.py), [main.py](variants/pyi-974aaf0c/main.py), [greet.py](variants/spec-98ef28e4/greet.py) created; verification pending |
| `.cgi` | [hello.cgi](variants/cgi-89feb572/hello.cgi) syntax and behavior verified |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.gyp` | [hello.gyp](variants/gyp-1f20e4eb/hello.gyp) created; verification pending |
| `.gypi` | [hello.gypi](variants/gypi-f4577eb6/hello.gypi) created; verification pending |
| `.lmi` | The Python canonical association is known, but the specific producer of this suffix is not documented by an identified primary source; an arbitrary alias is not assumed. |
| `.py3` | [hello.py3](variants/py3-2398b90a/hello.py3) syntax and behavior verified |
| `.pyde` | [hello.pyde](variants/pyde-38b52298/hello.pyde) created; verification pending |
| `.pyi` | [hello.pyi](variants/pyi-974aaf0c/hello.pyi) created; verification pending |
| `.pyp` | [hello.pyp](variants/pyp-ef387d94/hello.pyp) created; verification pending |
| `.pyt` | [hello.pyt](variants/pyt-b91dfe22/hello.pyt) created; verification pending |
| `.pyw` | [hello.pyw](variants/pyw-9952e8fc/hello.pyw) syntax and behavior verified |
| `.rpy` | [hello.rpy](variants/rpy-69e587c6/hello.rpy) created; verification pending |
| `.spec` | [hello.spec](variants/spec-98ef28e4/hello.spec) created; verification pending |
| `.tac` | [hello.tac](variants/tac-49a38cd6/hello.tac) created; verification pending |
| `.wsgi` | [hello.wsgi](variants/wsgi-89e83bb6/hello.wsgi) syntax and behavior verified |
| `.xpy` | The Python canonical association is known, but the specific producer of this suffix is not documented by an identified primary source; an arbitrary alias is not assumed. |
