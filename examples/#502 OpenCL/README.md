# #502 OpenCL

Voce canonica `OpenCL`, tipo `programming`, language_id `263`, gruppo Linguist `C`.

## Obiettivo

Il kernel scrive i 13 byte ASCII di `Hello, World!` nel buffer `output`, usando i global ID da 0 a 12.

## Toolchain e riproduzione

PoCL 5.0+debian, compilatore LLVM 16.0.6, PyOpenCL 2023.1.3, NumPy 1.26.4 e Python 3.12.3 su Ubuntu 24.04 WSL2 x86_64. Il runtime espone un dispositivo OpenCL CPU software. La prova seleziona esplicitamente PoCL e non richiede una GPU fisica.

Prerequisiti Ubuntu: `pocl-opencl-icd`, `python3-pyopencl` e il loader ICD OpenCL. Il checker e i sorgenti non installano package.

Dalla cartella dell'esempio, con le cache in una cartella di lavoro esterna al corpus:

```sh
mkdir -p /path/to/cache/pocl /path/to/cache/pyopencl
POCL_CACHE_DIR=/path/to/cache/pocl PYOPENCL_CACHE_DIR=/path/to/cache/pyopencl python3 verify_runtime.py hello.cl
POCL_CACHE_DIR=/path/to/cache/pocl PYOPENCL_CACHE_DIR=/path/to/cache/pyopencl python3 verify_runtime.py variants/opencl-1927a002/hello.opencl
```

Sostituire `/path/to/cache` con una propria cartella di lavoro. La precedente verifica del frontend Clang rimane riproducibile con `clang -x cl -cl-std=CL1.2 -fsyntax-only hello.cl`.

## Stato ed evidenza

Artefatti creati, sintassi verificata, semantica verificata per entrambe le estensioni.

`verify_runtime.py` legge ogni sorgente originale senza modificarlo, lo compila come OpenCL C 1.2, crea un buffer OpenCL e invia 13 work-item. Il readback reale produce esattamente `Hello, World!`. Il checker verifica anche che otto byte sentinella successivi rimangano invariati, quindi completa la coda del runtime.

[Log runtime](verification/runtime.json) con versioni, device effettivo, comandi, exit code, output, hash delle librerie native e dei file. [Log della variante](variants/opencl-1927a002/verification/runtime.json) registra separatamente il build e il dispatch del file `.opencl`. Le prove precedenti di sola sintassi restano in [clang.json](verification/clang.json) e nel log `native.json` della variante.

## Fonti primarie

- [Khronos OpenCL C](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html)
- [Driver CPU ufficiali PoCL](https://portablecl.org/docs/html/drivers.html)
- [PyOpenCL originale](https://documen.tician.de/pyopencl/)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.cl` | [hello.cl](hello.cl) sintassi e semantica verificate |
| `.opencl` | [hello.opencl](variants/opencl-1927a002/hello.opencl) sintassi e semantica verificate |
