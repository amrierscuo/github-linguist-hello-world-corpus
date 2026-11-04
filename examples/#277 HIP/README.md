# #277 HIP

Voce canonica `HIP`, tipo `programming`, language_id `674379998`.

Run a HIP kernel that writes thirteen byte ASCII on GPU, copy them to the host side and compare the greeting.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires HIP/ROCm or compatible NVIDIA backend, hipcc and GPU/runtime available. The code controls allocation, launch, synchronization, copy and release errors.

Comando/procedura from the directory of the example, unless explicit indications:

```text
hipcc hello.hip -o build/hello; ./build/hello
```

Expected result: Kernel executed; exact readback Hello, World!; exit 0.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The greeting comes from bytes written by the kernel. The compilation as normal C++ would ignore semantica/device HIP and is not presented as a verification. Hardware/toolchain absent.

Remaining requirements:

- HIP compiler, compatible GPU and HIP runtime are not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html)
- [https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/examples.html](https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/examples.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hip` | [hello.hip](hello.hip) created; verification pending |
