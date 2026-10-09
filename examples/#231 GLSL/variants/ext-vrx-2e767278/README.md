# GLSL .vrx

Stadio originale `vert`. File: `hello.vrx`.

Stato: sintassi verificata, semantica pendente.

Da questa cartella, con gli strumenti installati e un output temporaneo fuori dal corpus:

```sh
glslangValidator -V --target-env vulkan1.2 -S vert hello.vrx -o <output>/hello.spv
spirv-val --target-env vulkan1.2 <output>/hello.spv
```

Esecuzione della pipeline Vulkan dello stadio vert ancora pendente; compilazione e validazione SPIR-V riuscite per questo file.

[Log reale](../../verification/opengl_native.json) con versioni, timestamp UTC, comandi, exit/stdout/stderr, SHA256 del sorgente e risultati per file. I byte degli shader sono invariati. [Procedura principale](../../README.md).

Fonti: [GLSL](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf), [glslang](https://github.com/KhronosGroup/glslang), [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools).
