# #229 GDShader

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare un shader canvas_item e rappresentare i 13 byte di Hello, World! in bande grayscale.

L’array costante del saluto viene letto dal fragment shader, non è un commento. check_shader.gd assegna il codice a Shader e richiede la reflection; il backend Dummy originale chiama davvero ShaderCompiler::compile. Il log verifica il parser/compilatore, non il rendering GPU.

## Toolchain e riproduzione

Godot Engine 4.7.2.stable.official.ed1daf0bf Windows x64, compiler Dummy headless

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
godot --headless --path . --script check_shader.gd
```

```text
Con renderer grafico, assegnare hello.gdshader a un CanvasItem con UV.x da 0 a 1 ed exposure=1.
```

## Risultato atteso e stato

Compiler accetta lo shader e riflette exposure; il rendering atteso ha 13 bande con canali RGB uguali ai rispettivi byte divisi per 255.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Rendering e lettura dei pixel su un backend GPU non eseguiti; verifica semantica dell’output visivo pendente.

## Fonti primarie

- https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html
- https://github.com/godotengine/godot/blob/4.7/servers/rendering/dummy/storage/material_storage.cpp

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gdshader` | [hello.gdshader](hello.gdshader), [consumer.gdshader](variants/ext-gdshaderinc-2e6764736861646572696e63/consumer.gdshader) creato, verifiche pendenti |
| `.gdshaderinc` | [hello.gdshaderinc](variants/ext-gdshaderinc-2e6764736861646572696e63/hello.gdshaderinc) creato, verifiche pendenti |
