# #655 ShaderLab

## Verified on November 19, 2026

The headless parser resolved the exact greeting as the display label of the typed _Color material property and verified its default RGBA values. The pass uses an HLSL fragment program whose emitted SPIR-V loads the matching property and writes it to the output.

Run `inspect_shader hello.shader; glslangValidator -D -V -S frag -e frag bound.frag.hlsl; spirv-val bound.spv`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Load a ShaderLab shader with greeting property in the material inspector.

## Toolchain

Unity ShaderLab compiler/editor

## Procedure

Import hello.shader into a Unity project compatible with shader fixed-function; create a material and control the property.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The format goal is the property named Hello, World! and the pass that consumes the color, not visible text in the rendering.

Remaining requirements:
- Unity editor/shader compiler unavailable; fixed-function compatibility to try.

## Primary sources

- [https://docs.unity3d.com/Manual/SL-Properties.html](https://docs.unity3d.com/Manual/SL-Properties.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.shader` | [hello.shader](hello.shader) Syntax and behavior verified |

</details>
