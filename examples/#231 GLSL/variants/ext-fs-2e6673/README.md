# GLSL .fs

Stadio originale `frag`. File: `hello.fs`.

Status: syntax and behavior verified in OpenGL.

From this folder, with the installed tools and a temporary output out of the corpus:

```sh
glslangValidator -V --target-env vulkan1.2 -S frag hello.fs -o <output>/hello.spv
spirv-val --target-env vulkan1.2 <output>/hello.spv
```

verified native execution separately for this file. With Python, ModernGL 5.12.0, glcontext 3.0.0 and EGL/Mesa available:

```sh
LIBGL_ALWAYS_SOFTWARE=1 python ../../verification/render_opengl.py --stage frag hello.fs
```

Readback RGB8 esatto dei 13 code point ASCII.

[Log reale](../../verification/opengl_native.json) records versions, UTC timestamp, commands, exit codes, stdout/stderr, source SHA256 and per-file results. The shader bytes are unchanged. [Procedura principale](../../README.md).

Sources: [GLSL](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf), [glslang](https://github.com/KhronosGroup/glslang), [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools).
