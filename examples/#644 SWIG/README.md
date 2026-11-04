# #644 SWIG

Generate a binding SWIG C/Python and invoke greeting.

## Toolchain

SWIG Version 4.1.0

Compiled with g++ [x86_64-pc-linux-gnu]

Configured options: +pcre

Please see https://www.swig.org for reporting bugs and further information; Python 3.12.3; GCC13.3.0

## Procedure

swig -python -outdir build -o build/hello_wrap.c hello.i; gcc -shared -fPIC -I<python3.12-headers> build/hello_wrap.c -o build/_hello.so; PYTHONPATH=build python3 verify.py

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:23:07.256159+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://swig.org/Doc4.3/SWIGDocumentation.html](https://swig.org/Doc4.3/SWIGDocumentation.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.i` | [hello.i](hello.i) verified |
| `.swg` | [hello.swg](variants/swg-a3424d42/hello.swg) created; verification pending |
| `.swig` | [hello.swig](variants/swig-b750f324/hello.swig) created; verification pending |
