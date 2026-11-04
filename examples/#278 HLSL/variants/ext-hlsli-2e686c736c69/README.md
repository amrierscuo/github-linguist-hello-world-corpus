# 0278 HLSL: variant `.hlsli`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. FXC compiled the compute shader and all three include consumers. Direct3D 11 WARP dispatched each shader and read back the expected greeting. The separate Direct3D 10 Effects check rendered the original effect and decoded the same greeting from its pixels. [Evidence](../../verification/native_20261104_hlsl_result.json).

Role: Includes HLSL with shared data and function, without entry point.

Type: **adapted**. Starting model: examples/#278 HLSL/hello.hlsl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
dxc -T cs_6_0 -E main -I . consumer.hlsl -Fo <output>/hello.dxil; eseguire il compute in un harness GPU.
```

Expected result: Includes compiled in the consumer; buffer of 13 code point Hello, World!.

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
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-preprocessor](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-preprocessor)
- [https://docs.unity3d.com/Manual/SL-BuiltinIncludes.html](https://docs.unity3d.com/Manual/SL-BuiltinIncludes.html)
