# GLSL .gshader

Stadio originale `geom`. File: `hello.gshader`.

Stato: sintassi e semantica verificate in OpenGL.

Da questa cartella, con gli strumenti installati e un output temporaneo fuori dal corpus:

```sh
glslangValidator -V --target-env vulkan1.2 -S geom hello.gshader -o <output>/hello.spv
spirv-val --target-env vulkan1.2 <output>/hello.spv
```

Esecuzione nativa verificata separatamente per questo file. Con Python, ModernGL 5.12.0, glcontext 3.0.0 ed EGL/Mesa disponibili:

```sh
LIBGL_ALWAYS_SOFTWARE=1 python ../../verification/render_opengl.py --stage geom hello.gshader
```

Transform feedback13 float, query 13 primitive, recupero ASCII esatto Hello, World!, errore<1e-6.

[Log reale](../../verification/opengl_native.json) con versioni, timestamp UTC, comandi, exit/stdout/stderr, SHA256 del sorgente e risultati per file. I byte degli shader sono invariati. [Procedura principale](../../README.md).

Fonti: [GLSL](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf), [glslang](https://github.com/KhronosGroup/glslang), [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools).
