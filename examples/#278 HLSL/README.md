# #278 HLSL

Voce canonica `HLSL`, tipo `programming`, language_id `145`.

Compilare un compute shader HLSL che scrive tredici codici ASCII in un RWStructuredBuffer.

## Toolchain e riproduzione

Official Microsoft DirectX Shader Compiler — dxcompiler.dll: 1.9(5512-01b62ad4)(1.9.2609.5) - 1.9.2609.5 (01b62ad47). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Microsoft DirectX Shader Compiler ufficiale, release portable dxc_2026_09_29 con dxcompiler.dll 1.9.2609.5. Il prodotto DXIL resta in build.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
dxc -T cs_6_0 -E main -Fo build/hello.dxil hello.hlsl
```

Risultato atteso: Compilazione exit 0; runtime futuro ricostruisce Hello, World! da tredici uint.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Il compiler autentico accetta il sorgente e genera bytecode. La semantica resta pendente: occorre dispatch di un gruppo di 16 thread e readback dei primi tredici uint su Direct3D compatibile. Non viene dedotta dai soli valori nel sorgente.

Requisiti residui:

- Shader compiled; compute dispatch/readback on a compatible Direct3D runtime is not performed.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/microsoft/DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hlsl` | [hello.hlsl](hello.hlsl), [consumer.hlsl](variants/ext-cginc-2e6367696e63/consumer.hlsl), [consumer.hlsl](variants/ext-fxh-2e667868/consumer.hlsl), [consumer.hlsl](variants/ext-hlsli-2e686c736c69/consumer.hlsl) creato, verifiche pendenti |
| `.cginc` | [hello.cginc](variants/ext-cginc-2e6367696e63/hello.cginc) creato, verifiche pendenti |
| `.fx` | [hello.fx](variants/ext-fx-2e6678/hello.fx) creato, verifiche pendenti |
| `.fxh` | [hello.fxh](variants/ext-fxh-2e667868/hello.fxh) creato, verifiche pendenti |
| `.hlsli` | [hello.hlsli](variants/ext-hlsli-2e686c736c69/hello.hlsli) creato, verifiche pendenti |
