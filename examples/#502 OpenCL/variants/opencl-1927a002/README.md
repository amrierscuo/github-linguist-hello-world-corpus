# #502 OpenCL variante .opencl

Il file `hello.opencl` è una copia byte-identica del sorgente originale `hello.cl`; il test nativo è stato eseguito separatamente sul suo percorso.

Stato individuale: artefatto creato, sintassi verificata, semantica verificata.

Dalla directory principale dell'esempio:

```sh
python3 verify_runtime.py variants/opencl-1927a002/hello.opencl
```

Toolchain, prerequisiti e cache esterne sono descritti nel [README principale](../../README.md). PoCL 5.0+debian compila OpenCL C 1.2 sul dispositivo CPU, esegue 13 work-item e il readback produce `Hello, World!`. Otto byte sentinella restano invariati. Questo risultato riguarda l'esecuzione CPU software.

[Prova runtime](verification/runtime.json) con comando reale, versioni, exit code 0, output e hash. La prova precedente di sola sintassi è conservata in [native.json](verification/native.json).

Fonti primarie: [Khronos OpenCL C](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html), [PoCL](https://portablecl.org/docs/html/drivers.html), [PyOpenCL](https://documen.tician.de/pyopencl/).
