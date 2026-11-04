# 0278 HLSL: variant `.fx`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Load existing compiled unchanged Effects sample; apply its native Direct3D 10 pass, render a full-screen triangle to a 13 x 1 UNORM texture, read RGBA and compare decoded greeting. [Evidence](../../verification/native_20261104_hlsl_fx_result.json).

Role: Effect HLSL Effects10 with technique/pass and shader pixels; do not compute shader hlsl renamed.

Type: **adapted**. Starting model: examples/#278 HLSL/hello.hlsl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
FXC: fxc /T fx_4_0 /Fo <output>/hello.fxo hello.fx; caricare l’effetto in un harness D3D10 e leggere 13 pixel.
```

Expected result: Accepted effect; 13 pixel codify Hello, World!.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/microsoft/DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/windows/win32/direct3d10/d3d10-effect-state-management](https://learn.microsoft.com/en-us/windows/win32/direct3d10/d3d10-effect-state-management)
