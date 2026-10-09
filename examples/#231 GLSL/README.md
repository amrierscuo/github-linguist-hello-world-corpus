# #231 GLSL OpenGL rendering

Il fragment shader GLSL 450 originale viene compilato ed eseguito in una pipeline OpenGL 4.5. Il framebuffer 13x1 RGB8 contiene il saluto `Hello, World!`, un byte ASCII per pixel e lo stesso valore in tutti e tre i canali RGB.

Tipo canonico `programming`, language_id `124`.

## Toolchain e riproduzione

Compilazione statica con glslang 15.1.0 e SPIRV-Tools 2025.1. La nuova esecuzione usa Python 3.12.3, ModernGL 5.12.0 e glcontext 3.0.0 in Ubuntu 24.04 WSL2, Mesa 25.2.8 e llvmpipe (LLVM 20.1.2). Il contesto EGL riporta OpenGL 4.5 Core Profile.

Il driver [render_opengl.py](verification/render_opengl.py) richiede EGL/Mesa e un contesto OpenGL 4.5; le dipendenze Python si installano in un ambiente isolato fuori dal clone, ad esempio:

```sh
python3 -m venv /tmp/corpus-glsl-venv
/tmp/corpus-glsl-venv/bin/python -m pip install moderngl==5.12.0 glcontext==3.0.0
```

Dalla cartella di questo esempio:

```sh
LIBGL_ALWAYS_SOFTWARE=1 /tmp/corpus-glsl-venv/bin/python verification/render_opengl.py --stage frag hello.frag
```

Il driver carica il file originale senza modificarne il testo, lo collega a un vertex shader di fixture, disegna un triangolo che copre il target e legge tutti i 39 byte RGB dal framebuffer. Confronta byte per byte il risultato atteso. Non ricostruisce i pixel leggendo l'array del sorgente.

Per una variante geometry originale, il driver registra transform feedback e una query nativa sul numero di primitive, per esempio:

```sh
LIBGL_ALWAYS_SOFTWARE=1 /tmp/corpus-glsl-venv/bin/python verification/render_opengl.py --stage geom variants/ext-geo-2e67656f/hello.geo
```

Questo produce 13 float, legge il buffer effettivo della pipeline e verifica 13 primitive emesse, i13byte ASCII recuperati e un errore numerico inferiore a 1e-6.

La compilazione SPIR-V rimane riproducibile con una directory temporanea di output:

```sh
glslangValidator -V --target-env vulkan1.2 -S frag hello.frag -o /tmp/corpus-hello.spv
spirv-val --target-env vulkan1.2 /tmp/corpus-hello.spv
```

## Stato ed evidenza

Sintassi e semantica del campione principale verificate. Tutti i 23 shader del corpus sono stati compilati separatamente con lo stadio esplicito e il loro SPIR-V è stato validato. I 9 fragment e le 4 varianti geometry sono stati caricati ed eseguiti singolarmente nella pipeline OpenGL.

Le 6 varianti vertex, le 2 tessellation e le 2 ray-tracing hanno solo sintassi verificata; la loro esecuzione rimane pendente. Le prove sono specifiche per file e stadio.

Il [log nativo](verification/opengl_native.json) conserva comandi effettivi, versioni, timestamp UTC, exit/stdout/stderr, SHA256 e misure. Il readback RGB8 è esatto; i 13 code point sono `72,101,108,108,111,44,32,87,111,114,108,100,33`.

La verifica usa un renderer software reale OpenGL; non attesta un'esecuzione Vulkan né hardware GPU fisico. La [precedente prova SPIR-V](verification/toolchain.json) rimane conservata. Dipendenze e prodotti compilati restano nella directory di lavoro.

## Fonti primarie

- [GLSL 450 Khronos](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf)
- [glslang](https://github.com/KhronosGroup/glslang)
- [SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools)
- [Context in ModernGL](https://moderngl.readthedocs.io/en/latest/reference/moderngl.html)
- [Framebuffer readback](https://moderngl.readthedocs.io/en/latest/reference/framebuffer.html)
- [Transform feedback](https://moderngl.readthedocs.io/en/latest/reference/vertex_array.html)
- [Mesa e renderer software](https://docs.mesa3d.org/envvars.html)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.glsl` | [hello.glsl](variants/ext-glsl-2e676c736c/hello.glsl) sintassi e semantica verificate |
| `.fp` | [hello.fp](variants/ext-fp-2e6670/hello.fp) sintassi e semantica verificate |
| `.frag` | [hello.frag](hello.frag) sintassi e semantica verificate |
| `.frg` | [hello.frg](variants/ext-frg-2e667267/hello.frg) sintassi e semantica verificate |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) sintassi e semantica verificate |
| `.fsh` | [hello.fsh](variants/ext-fsh-2e667368/hello.fsh) sintassi e semantica verificate |
| `.fshader` | [hello.fshader](variants/ext-fshader-2e66736861646572/hello.fshader) sintassi e semantica verificate |
| `.geo` | [hello.geo](variants/ext-geo-2e67656f/hello.geo) sintassi e semantica verificate |
| `.geom` | [hello.geom](variants/ext-geom-2e67656f6d/hello.geom) sintassi e semantica verificate |
| `.glslf` | [hello.glslf](variants/ext-glslf-2e676c736c66/hello.glslf) sintassi e semantica verificate |
| `.glslv` | [hello.glslv](variants/ext-glslv-2e676c736c76/hello.glslv) sintassi verificata |
| `.gs` | [hello.gs](variants/ext-gs-2e6773/hello.gs) sintassi e semantica verificate |
| `.gshader` | [hello.gshader](variants/ext-gshader-2e67736861646572/hello.gshader) sintassi e semantica verificate |
| `.rchit` | [hello.rchit](variants/ext-rchit-2e7263686974/hello.rchit) sintassi verificata |
| `.rmiss` | [hello.rmiss](variants/ext-rmiss-2e726d697373/hello.rmiss) sintassi verificata |
| `.shader` | [hello.shader](variants/ext-shader-2e736861646572/hello.shader) sintassi e semantica verificate |
| `.tesc` | [hello.tesc](variants/ext-tesc-2e74657363/hello.tesc) sintassi verificata |
| `.tese` | [hello.tese](variants/ext-tese-2e74657365/hello.tese) sintassi verificata |
| `.vert` | [hello.vert](variants/ext-vert-2e76657274/hello.vert) sintassi verificata |
| `.vrx` | [hello.vrx](variants/ext-vrx-2e767278/hello.vrx) sintassi verificata |
| `.vs` | [hello.vs](variants/ext-vs-2e7673/hello.vs) sintassi verificata |
| `.vsh` | [hello.vsh](variants/ext-vsh-2e767368/hello.vsh) sintassi verificata |
| `.vshader` | [hello.vshader](variants/ext-vshader-2e76736861646572/hello.vshader) sintassi verificata |
