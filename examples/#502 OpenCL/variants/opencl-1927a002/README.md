# #502 OpenCL variante .opencl

The `hello.opencl` file is a byte-identical copy of the original `hello.cl` source; the native test was performed separately on its path.

Individual state: artifact created, syntax verified, behavior verified.

From the main directory of the example:

```sh
python3 verify_runtime.py variants/opencl-1927a002/hello.opencl
```

Toolchain, prerequisiti e cache esterne sono descritti nel [README principale](../../README.md). PoCL 5.0+debian compila OpenCL C 1.2 sul dispositivo CPU, esegue 13 work-item e il readback produce `Hello, World!`. Otto byte sentinella restano invariati. Questo risultato riguarda l'esecuzione CPU software.

[Prova runtime](verification/runtime.json) with real command, versions, exit code 0, output and hash. The previous test of only syntax is preserved in [native.json](verification/native.json).

Primary sources: [Khronos OpenCL C](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html), [PoCL](https://portablecl.org/docs/html/drivers.html), [PyOpenCL](https://documen.tician.de/pyopencl/).
