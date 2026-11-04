# #231 GLSL OpenGL rendering

The original fragment shader GLSL 450 is compiled and executed in an OpenGL 4.5 pipeline. The framebuffer 13x1 RGB8 contains the `Hello, World!` greeting, a ASCII byte per pixel and the same value in all three RGB channels.

Canonical type `programming`, language_id `124`.

## Toolchain and reproduction

Compilazione statica con glslang 15.1.0 e SPIRV-Tools 2025.1. La nuova esecuzione usa Python 3.12.3, ModernGL 5.12.0 e glcontext 3.0.0 in Ubuntu 24.04 WSL2, Mesa 25.2.8 e llvmpipe (LLVM 20.1.2). Il contesto EGL riporta OpenGL 4.5 Core Profile.

The [render_opengl.py](verification/render_opengl.py) driver requires EGL/Mesa and an OpenGL 4.5 context; Python dependencies are installed in an isolated environment outside the clone, for example:

```sh
python3 -m venv /tmp/corpus-glsl-venv
/tmp/corpus-glsl-venv/bin/python -m pip install moderngl==5.12.0 glcontext==3.0.0
```

From the folder of this example:

```sh
LIBGL_ALWAYS_SOFTWARE=1 /tmp/corpus-glsl-venv/bin/python verification/render_opengl.py --stage frag hello.frag
```

The driver uploads the original file without modifying the text, connects it to a fixture shader vertex, draws a triangle covering the target and reads all 39 byte RGB by framebuffer.

For an original geometry variant, the driver records transform feedback and a native query on the primitive number, for example:

```sh
LIBGL_ALWAYS_SOFTWARE=1 /tmp/corpus-glsl-venv/bin/python verification/render_opengl.py --stage geom variants/ext-geo-2e67656f/hello.geo
```

This produces 13 float, reads the actual buffer of the pipeline and verifies primitive emitted 13, i13byte ASCII recovered and a numerical error less than 1e-6.

The SPIR -V compilation remains reproducible with a temporary output directory:

```sh
glslangValidator -V --target-env vulkan1.2 -S frag hello.frag -o /tmp/corpus-hello.spv
spirv-val --target-env vulkan1.2 /tmp/corpus-hello.spv
```

## Status and evidence

Sintassi e semantica del campione principale verificate. Tutti i 23 shader del corpus sono stati compilati separatamente con lo stadio esplicito e il loro SPIR-V è stato validato. I 9 fragment e le 4 varianti geometry sono stati caricati ed eseguiti singolarmente nella pipeline OpenGL.

The 6 variants vertex, 2 tessellation and 2 ray-tracing have only syntax verified; their execution remains pending.

Il [log nativo](verification/opengl_native.json) conserva comandi effettivi, versioni, timestamp UTC, exit/stdout/stderr, SHA256 e misure. Il readback RGB8 è esatto; i 13 code point sono `72,101,108,108,111,44,32,87,111,114,108,100,33`.

La verifica usa un renderer software reale OpenGL; non attesta un'esecuzione Vulkan né hardware GPU fisico. La [precedente prova SPIR-V](verification/toolchain.json) rimane conservata. Dipendenze e prodotti compilati restano nella directory di lavoro.

## Primary sources

- [GLSL 450 Khronos](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf)
- [glslang](https://github.com/KhronosGroup/glslang)
- [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools)
- [Context in ModernGL](https://moderngl.readthedocs.io/en/latest/reference/moderngl.html)
- [Framebuffer readback](https://moderngl.readthedocs.io/en/latest/reference/framebuffer.html)
- [Transform feedback](https://moderngl.readthedocs.io/en/latest/reference/vertex_array.html)
- [Mesa e renderer software](https://docs.mesa3d.org/envvars.html)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.glsl` | [hello.glsl](variants/ext-glsl-2e676c736c/hello.glsl) syntax and behavior verified |
| `.fp` | [hello.fp](variants/ext-fp-2e6670/hello.fp) syntax and behavior verified |
| `.frag` | [hello.frag](hello.frag) syntax and behavior verified |
| `.frg` | [hello.frg](variants/ext-frg-2e667267/hello.frg) syntax and behavior verified |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) syntax and behavior verified |
| `.fsh` | [hello.fsh](variants/ext-fsh-2e667368/hello.fsh) syntax and behavior verified |
| `.fshader` | [hello.fshader](variants/ext-fshader-2e66736861646572/hello.fshader) syntax and behavior verified |
| `.geo` | [hello.geo](variants/ext-geo-2e67656f/hello.geo) syntax and behavior verified |
| `.geom` | [hello.geom](variants/ext-geom-2e67656f6d/hello.geom) syntax and behavior verified |
| `.glslf` | [hello.glslf](variants/ext-glslf-2e676c736c66/hello.glslf) syntax and behavior verified |
| `.glslv` | [hello.glslv](variants/ext-glslv-2e676c736c76/hello.glslv) syntax verified |
| `.gs` | [hello.gs](variants/ext-gs-2e6773/hello.gs) syntax and behavior verified |
| `.gshader` | [hello.gshader](variants/ext-gshader-2e67736861646572/hello.gshader) syntax and behavior verified |
| `.rchit` | [hello.rchit](variants/ext-rchit-2e7263686974/hello.rchit) syntax verified |
| `.rmiss` | [hello.rmiss](variants/ext-rmiss-2e726d697373/hello.rmiss) syntax verified |
| `.shader` | [hello.shader](variants/ext-shader-2e736861646572/hello.shader) syntax and behavior verified |
| `.tesc` | [hello.tesc](variants/ext-tesc-2e74657363/hello.tesc) syntax verified |
| `.tese` | [hello.tese](variants/ext-tese-2e74657365/hello.tese) syntax verified |
| `.vert` | [hello.vert](variants/ext-vert-2e76657274/hello.vert) syntax verified |
| `.vrx` | [hello.vrx](variants/ext-vrx-2e767278/hello.vrx) syntax verified |
| `.vs` | [hello.vs](variants/ext-vs-2e7673/hello.vs) syntax verified |
| `.vsh` | [hello.vsh](variants/ext-vsh-2e767368/hello.vsh) syntax verified |
| `.vshader` | [hello.vshader](variants/ext-vshader-2e76736861646572/hello.vshader) syntax verified |
