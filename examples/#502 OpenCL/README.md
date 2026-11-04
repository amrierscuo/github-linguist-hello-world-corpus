# #502 OpenCL

Voce canonica `OpenCL`, tipo `programming`, language_id `263`, gruppo Linguist `C`.

## Goal

The kernel writes 13 byte ASCII of `Hello, World!` in the `output` buffer, using global ID from 0 to 12.

## Toolchain and reproduction

PoCL 5.0+debian, compilatore LLVM 16.0.6, PyOpenCL 2023.1.3, NumPy 1.26.4 e Python 3.12.3 su Ubuntu 24.04 WSL2 x86_64. Il runtime espone un dispositivo OpenCL CPU software. La prova seleziona esplicitamente PoCL e non richiede una GPU fisica.

Prerequisites Ubuntu: `pocl-opencl-icd`, `python3-pyopencl` and ICD OpenCL loader. Checker and sources do not install package.

From the example folder, with caches in a workbook external to the corpus:

```sh
mkdir -p /path/to/cache/pocl /path/to/cache/pyopencl
POCL_CACHE_DIR=/path/to/cache/pocl PYOPENCL_CACHE_DIR=/path/to/cache/pyopencl python3 verify_runtime.py hello.cl
POCL_CACHE_DIR=/path/to/cache/pocl PYOPENCL_CACHE_DIR=/path/to/cache/pyopencl python3 verify_runtime.py variants/opencl-1927a002/hello.opencl
```

Replace `/path/to/cache` with its own workbook. The previous Clang frontend verification remains reproducible with `clang -x cl -cl-std=CL1.2 -fsyntax-only hello.cl`.

## Status and evidence

Created artifacts, syntax verified, behavior verified for both extensions.

`verify_runtime.py` reads each original source without modifying it, compiles it as OpenCL C 1.2, creates an OpenCL buffer and sends 13 work-item. The real readback produces exactly `Hello, World!`. The checker also checks that eight later sentinel bytes remain unchanged, then completes the runtime queue.

[Log runtime](verification/runtime.json) con versioni, device effettivo, comandi, exit code, output, hash delle librerie native e dei file. [Log della variante](variants/opencl-1927a002/verification/runtime.json) registra separatamente il build e il dispatch del file `.opencl`. Le prove precedenti di sola sintassi restano in [clang.json](verification/clang.json) e nel log `native.json` della variante.

## Primary sources

- [Khronos OpenCL C](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html)
- [Driver CPU ufficiali PoCL](https://portablecl.org/docs/html/drivers.html)
- [PyOpenCL originale](https://documen.tician.de/pyopencl/)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.cl` | [hello.cl](hello.cl) syntax and behavior verified |
| `.opencl` | [hello.opencl](variants/opencl-1927a002/hello.opencl) syntax and behavior verified |
