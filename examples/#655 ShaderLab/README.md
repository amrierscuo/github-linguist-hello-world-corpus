# #655 ShaderLab

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
| `.shader` | [hello.shader](hello.shader) created; verification pending |
