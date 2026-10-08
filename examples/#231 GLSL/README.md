# #231 GLSL

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Compilare un fragment shader GLSL 450 che codifica Hello, World! nei primi 13 pixel grayscale.

Il saluto è l’array di interi effettivamente indicizzato da gl_FragCoord.x. Il modulo SPIR-V è generato dal compiler originale e validato. Non è stato avviato un renderer Vulkan né misurato l’output GPU.

## Toolchain e riproduzione

Khronos glslang 15.1.0 e SPIRV-Tools 2025.1, pacchetti Ubuntu

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
glslangValidator -V hello.frag -o hello.spv
spirv-val hello.spv
```

```text
Con pipeline Vulkan offline, renderizzare un target 13×1 con hello.frag.
```

## Risultato atteso e stato

Compilazione e validazione SPIR-V exit 0; rendering atteso: valori RGB uguali ai 13 byte ASCII divisi per 255.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Il contratto visivo dei 13 pixel non è stato eseguito su una pipeline GPU; semantica pendente.

## Fonti primarie

- https://github.com/KhronosGroup/glslang
- https://github.com/KhronosGroup/SPIRV-Tools
- https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.glsl` | [hello.glsl](variants/ext-glsl-2e676c736c/hello.glsl) creato, verifiche pendenti |
| `.fp` | [hello.fp](variants/ext-fp-2e6670/hello.fp) creato, verifiche pendenti |
| `.frag` | [hello.frag](hello.frag) sintassi verificata |
| `.frg` | [hello.frg](variants/ext-frg-2e667267/hello.frg) creato, verifiche pendenti |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) creato, verifiche pendenti |
| `.fsh` | [hello.fsh](variants/ext-fsh-2e667368/hello.fsh) creato, verifiche pendenti |
| `.fshader` | [hello.fshader](variants/ext-fshader-2e66736861646572/hello.fshader) creato, verifiche pendenti |
| `.geo` | [hello.geo](variants/ext-geo-2e67656f/hello.geo) creato, verifiche pendenti |
| `.geom` | [hello.geom](variants/ext-geom-2e67656f6d/hello.geom) creato, verifiche pendenti |
| `.glslf` | [hello.glslf](variants/ext-glslf-2e676c736c66/hello.glslf) creato, verifiche pendenti |
| `.glslv` | [hello.glslv](variants/ext-glslv-2e676c736c76/hello.glslv) creato, verifiche pendenti |
| `.gs` | [hello.gs](variants/ext-gs-2e6773/hello.gs) creato, verifiche pendenti |
| `.gshader` | [hello.gshader](variants/ext-gshader-2e67736861646572/hello.gshader) creato, verifiche pendenti |
| `.rchit` | [hello.rchit](variants/ext-rchit-2e7263686974/hello.rchit) creato, verifiche pendenti |
| `.rmiss` | [hello.rmiss](variants/ext-rmiss-2e726d697373/hello.rmiss) creato, verifiche pendenti |
| `.shader` | [hello.shader](variants/ext-shader-2e736861646572/hello.shader) creato, verifiche pendenti |
| `.tesc` | [hello.tesc](variants/ext-tesc-2e74657363/hello.tesc) creato, verifiche pendenti |
| `.tese` | [hello.tese](variants/ext-tese-2e74657365/hello.tese) creato, verifiche pendenti |
| `.vert` | [hello.vert](variants/ext-vert-2e76657274/hello.vert) creato, verifiche pendenti |
| `.vrx` | [hello.vrx](variants/ext-vrx-2e767278/hello.vrx) creato, verifiche pendenti |
| `.vs` | [hello.vs](variants/ext-vs-2e7673/hello.vs) creato, verifiche pendenti |
| `.vsh` | [hello.vsh](variants/ext-vsh-2e767368/hello.vsh) creato, verifiche pendenti |
| `.vshader` | [hello.vshader](variants/ext-vshader-2e76736861646572/hello.vshader) creato, verifiche pendenti |
