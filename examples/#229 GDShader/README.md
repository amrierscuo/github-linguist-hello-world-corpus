# #229 GDShader

Compilare un shader canvas_item e rappresentare i 13 byte di Hello, World! in bande grayscale.

## Verifica reale

Godot 4.7.2 ufficiale; Mesa 25.2.8 llvmpipe OpenGL 4.5 software; Xvfb

```sh
LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a godot --path . --rendering-method gl_compatibility --rendering-driver opengl3 --audio-driver Dummy --script res://verify_render.gd -- res://hello.gdshader
```

**Sintassi e semantica verificate.** Godot 4.7.2 ufficiale renderizza realmente il CanvasItem con OpenGL 4.5 Mesa 25.2.8 llvmpipe, backend software. Readback del SubViewport 130x10: i 13 campioni RGB coincidono esattamente con i byte ASCII di Hello, World!. Anche il consumatore della variante .gdshaderinc supera la stessa prova. Il warning V-Sync è conservato nel log e non altera i pixel; audio Dummy esplicito.

[Log con comandi, output e hash](verification/render.json). La precedente prova compiler Dummy resta in [toolchain.json](verification/toolchain.json).

I pixel rappresentano i byte del saluto in scala di grigi; questa è la semantica del campione, senza testo disegnato dal driver.

![Pixel renderizzati dallo shader](verification/rendered-main.png)

## Fonti primarie

- [https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html)
- [https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp](https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp)
- [https://docs.godotengine.org/en/stable/classes/class_subviewport.html](https://docs.godotengine.org/en/stable/classes/class_subviewport.html)
- [https://docs.godotengine.org/en/stable/classes/class_viewporttexture.html](https://docs.godotengine.org/en/stable/classes/class_viewporttexture.html)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.gdshader` | [hello.gdshader](hello.gdshader), [consumer.gdshader](variants/ext-gdshaderinc-2e6764736861646572696e63/consumer.gdshader) sintassi e semantica verificate |
| `.gdshaderinc` | [hello.gdshaderinc](variants/ext-gdshaderinc-2e6764736861646572696e63/hello.gdshaderinc) sintassi e semantica verificate |
