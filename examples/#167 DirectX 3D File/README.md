# #167 DirectX 3D File

Import a DirectX .x text model with HelloWorld node and an original triangle.

## Toolchain

Assimp native importer ------------------------------------------------------ 
Open Asset Import Library ("Assimp", https://github.com/assimp/assimp) 
 -- Commandline toolchain --
------------------------------------------------------ 

Version 5.3 -debug -shared -st (GIT commit 0)

## Commands and procedure

assimp version; assimp info hello.x

## Expected result

Import exit 0; node HelloWorld, a mesh, 3 vertices and a face.

## Status

syntax and behavior verified.

The greeting is represented by the name of the node; this format contains geometry and non-print text. FrameTransformMatrix is identity. Assimp’s native DirectX importer really loads the file; the test covers pattern and counts, without declaring a graphical rendering.

Actual verification of 2026-10-08T11:56:11.594568+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://learn.microsoft.com/en-us/windows/win32/direct3d9/x-files--legacy-](https://learn.microsoft.com/en-us/windows/win32/direct3d9/x-files--legacy-)
- [https://github.com/assimp/assimp](https://github.com/assimp/assimp)
- [https://learn.microsoft.com/en-us/windows/win32/direct3d9/mesh](https://learn.microsoft.com/en-us/windows/win32/direct3d9/mesh)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.x` | [hello.x](hello.x) verified |
