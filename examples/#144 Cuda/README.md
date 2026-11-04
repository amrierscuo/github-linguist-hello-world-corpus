# #144 Cuda

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Launch a single CUDA thread that prints Hello, World! and sync the device.

The greeting comes from the __global__ kernel, launched with << 1, 1 >>>> cudaGetLastError and cudaDeviceSynchronize control the launch and flush the output; cuda cudeDeviceReset closes the context. The program returns error if the device or runtime does not work.

## Toolchain and reproduction

NVIDIA CUDA Toolkit/nvcc e GPU CUDA compatibile; versioni effettive da registrare

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
nvcc hello.cu -o hello
```

```text
./hello
```

## Expected result and status

stdout Hello, World! followed by newline; launch and synchronization without error.

Artifact created: yes. syntax verified: no. behavior verified: no.

The source is documented; native parser/compilatore/runtime has not been performed for this item.

Commitments: nvcc and an environment GPU CUDA verifiable are not prepared; compilation and execution device remain pending.

## Primary sources

- https://docs.nvidia.com/cuda/cuda-programming-guide/index.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cu` | [hello.cu](hello.cu), [consumer.cu](variants/ext-cuh-2e637568/consumer.cu) created; verification pending |
| `.cuh` | [hello.cuh](variants/ext-cuh-2e637568/hello.cuh) created; verification pending |
