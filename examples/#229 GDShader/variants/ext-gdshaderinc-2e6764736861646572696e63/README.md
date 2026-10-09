# 0229 GDShader — variante `.gdshaderinc`

Ruolo: Include GDShader Godot 4 con costanti e funzione, senza shader_type o entry point.

Tipo variante: **adapted**. Modello di partenza: examples/#229 GDShader/hello.gdshader; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Godot 4: aprire il progetto temporaneo con consumer.gdshader e compilare; renderizzare 13 campioni e decodificare il saluto.
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html)
- [https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp](https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)

## Esecuzione reale 2026-10-09

Godot 4.7.2 ufficiale renderizza realmente il CanvasItem con OpenGL 4.5 Mesa 25.2.8 llvmpipe, backend software. Readback del SubViewport 130x10: i 13 campioni RGB coincidono esattamente con i byte ASCII di Hello, World!. Anche il consumatore della variante .gdshaderinc supera la stessa prova. Il warning V-Sync è conservato nel log e non altera i pixel; audio Dummy esplicito.

```sh
LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a godot --path variants/ext-gdshaderinc-2e6764736861646572696e63 --rendering-method gl_compatibility --rendering-driver opengl3 --audio-driver Dummy --script res://verify_render.gd -- res://consumer.gdshader
```
