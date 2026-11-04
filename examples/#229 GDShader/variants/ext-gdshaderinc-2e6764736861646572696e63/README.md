# 0229 GDShader: variant `.gdshaderinc`

Role: Includes GDShader Godot 4 with constants and function, without shader_type or entry point.

Type: **adapted**. Starting model: examples/#229 GDShader/hello.gdshader; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Godot 4: aprire il progetto temporaneo con consumer.gdshader e compilare; renderizzare 13 campioni e decodificare il saluto.
```

Expected result: Hello, World!

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html)
- [https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp](https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)

## Recorded execution: October 9, 2026

Godot 4.7.2 ufficiale renderizza realmente il CanvasItem con OpenGL 4.5 Mesa 25.2.8 llvmpipe, backend software. Readback del SubViewport 130x10: i 13 campioni RGB coincidono esattamente con i byte ASCII di Hello, World!. Anche il consumatore della variante .gdshaderinc supera la stessa prova. Il warning V-Sync è conservato nel log e non altera i pixel; audio Dummy esplicito.

```sh
LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a godot --path variants/ext-gdshaderinc-2e6764736861646572696e63 --rendering-method gl_compatibility --rendering-driver opengl3 --audio-driver Dummy --script res://verify_render.gd -- res://consumer.gdshader
```
