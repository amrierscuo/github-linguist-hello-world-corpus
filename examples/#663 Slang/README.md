# #663 Slang

Slang generated C++ from the original compute shader. A native CPU host dispatched it and read back the exact ASCII greeting.

Canonical type: `programming`. Linguist language ID: `239357863`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with Slang 2026.19 and Zig C++ 0.15.2.

[Recorded commands, outputs and hashes](verification/native_20261104_slang_result.json).
[Earlier verification record](verification/result.json).

## Reproduce the check

In a scratch directory copy `hello.slang` and `verification/dispatch.cpp`. With the recorded Slang and Zig versions:

```sh
slangc hello.slang -entry main -target cpp -o generated_shader.cpp
zig c++ -O2 -std=c++17 dispatch.cpp -o dispatch.exe
./dispatch.exe
```

This verifies the CPU compute target. GPU dispatch is outside the scope of this run.

## Primary sources


## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.slang` | [hello.slang](hello.slang) | Syntax and behavior verified |
