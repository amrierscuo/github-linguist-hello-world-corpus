# GLSL .fsh

Stadio originale `frag`. File: `hello.fsh`.

Stato: sintassi e semantica verificate in OpenGL.

Da questa cartella, con gli strumenti installati e un output temporaneo fuori dal corpus:

```sh
glslangValidator -V --target-env vulkan1.2 -S frag hello.fsh -o <output>/hello.spv
spirv-val --target-env vulkan1.2 <output>/hello.spv
```

Esecuzione nativa verificata separatamente per questo file. Con Python, ModernGL 5.12.0, glcontext 3.0.0 ed EGL/Mesa disponibili:

```sh
LIBGL_ALWAYS_SOFTWARE=1 python ../../verification/render_opengl.py --stage frag hello.fsh
```

Readback RGB8 esatto dei 13 code point ASCII.

[Log reale](../../verification/opengl_native.json) con versioni, timestamp UTC, comandi, exit/stdout/stderr, SHA256 del sorgente e risultati per file. I byte degli shader sono invariati. [Procedura principale](../../README.md).

Fonti: [GLSL](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf), [glslang](https://github.com/KhronosGroup/glslang), [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools).
