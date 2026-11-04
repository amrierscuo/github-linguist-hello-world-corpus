# #734 Unity3D Asset

Upload an original Unity scene with GameObject greeting.

## Toolchain

Unity scene YAML reader/editor

## Procedure

Import hello.unity into a Unity project and control the GameObject Hello, World! with Transform.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The goal is the name of the object in the hierarchy, not a UI rendered text; no GUID or external scripts are inserted.

Remaining requirements:
- Unity editor/scene loader unavailable; compatibility of serialized pending fields.

## Primary sources

- [https://docs.unity3d.com/Manual/FormatDescription.html](https://docs.unity3d.com/Manual/FormatDescription.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.anim` | [hello.anim](variants/anim-785361ae/hello.anim) created; verification pending |
| `.asset` | [hello.asset](variants/asset-1e16658f/hello.asset) created; verification pending |
| `.mask` | [hello.mask](variants/mask-6a9aba18/hello.mask) created; verification pending |
| `.mat` | [hello.mat](variants/mat-6b850197/hello.mat) created; verification pending |
| `.meta` | [greeting.asset.meta](variants/meta-e10ebe20/greeting.asset.meta) created; verification pending |
| `.prefab` | [hello.prefab](variants/prefab-3814199a/hello.prefab) created; verification pending |
| `.unity` | [hello.unity](hello.unity) created; verification pending |
