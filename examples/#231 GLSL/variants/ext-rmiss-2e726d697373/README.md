# GLSL .rmiss

Stadio originale `rmiss`. File: `hello.rmiss`.

Status: syntax verified, behavior pendant.

From this folder, with the installed tools and a temporary output out of the corpus:

```sh
glslangValidator -V --target-env vulkan1.2 -S rmiss hello.rmiss -o <output>/hello.spv
spirv-val --target-env vulkan1.2 <output>/hello.spv
```

Execution of the Vulkan pipeline of the still pending rmiss stage; compilation and validation SPIR -V managed for this file.

[Log reale](../../verification/opengl_native.json) records versions, UTC timestamp, commands, exit codes, stdout/stderr, source SHA256 and per-file results. The shader bytes are unchanged. [Procedura principale](../../README.md).

Sources: [GLSL](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf), [glslang](https://github.com/KhronosGroup/glslang), [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools).
