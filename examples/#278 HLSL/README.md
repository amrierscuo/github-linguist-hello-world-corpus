# #278 HLSL

FXC compiled the compute shader and all three include consumers. Direct3D 11 WARP dispatched each shader and read back the expected greeting. The separate Direct3D 10 Effects check rendered the original effect and decoded the same greeting from its pixels.

Canonical type: `programming`. Linguist language ID: `145`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with Microsoft FXC 10.1, Windows SDK 10.0.26100.0, Direct3D WARP and Zig C++ 0.15.2.

[Recorded commands, outputs and hashes](verification/native_20261104_hlsl_result.json).
[Earlier verification record](verification/native.json).
[Direct3D Effects verification](verification/native_20261104_hlsl_fx_result.json).

## Reproduce the check

Use the FXC and Zig commands in the receipts in a scratch directory. `verification/dispatch.cpp` is the Direct3D 11 readback harness; the effect uses `verification/render_fx.cpp` and `verification/fullscreen_vs.hlsl`. Use the recorded source filenames and include paths. These checks use Windows software rendering; they do not require a physical GPU.

## Primary sources

- https://github.com/microsoft/DirectXShaderCompiler
- https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl
- https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer

## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.hlsl` | [hello.hlsl](hello.hlsl), [consumer.hlsl](variants/ext-cginc-2e6367696e63/consumer.hlsl), [consumer.hlsl](variants/ext-fxh-2e667868/consumer.hlsl), [consumer.hlsl](variants/ext-hlsli-2e686c736c69/consumer.hlsl) | Syntax and behavior verified |
| `.cginc` | [hello.cginc](variants/ext-cginc-2e6367696e63/hello.cginc) | Syntax and behavior verified |
| `.fx` | [hello.fx](variants/ext-fx-2e6678/hello.fx) | Syntax and behavior verified |
| `.fxh` | [hello.fxh](variants/ext-fxh-2e667868/hello.fxh) | Syntax and behavior verified |
| `.hlsli` | [hello.hlsli](variants/ext-hlsli-2e686c736c69/hello.hlsli) | Syntax and behavior verified |
