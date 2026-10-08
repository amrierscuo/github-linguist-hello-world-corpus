# 0278 HLSL — variante `.fx`

Ruolo: Effetto HLSL Effects10 con technique/pass e shader pixel; non compute shader hlsl rinominato.

Tipo variante: **adapted**. Modello di partenza: examples/#278 HLSL/hello.hlsl; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
FXC: fxc /T fx_4_0 /Fo <output>/hello.fxo hello.fx; caricare l’effetto in un harness D3D10 e leggere 13 pixel.
```

Risultato atteso: Effetto accettato; 13 pixel codificano Hello, World!.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/microsoft/DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)
- [https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/sm5-object-rwstructuredbuffer)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/windows/win32/direct3d10/d3d10-effect-state-management](https://learn.microsoft.com/en-us/windows/win32/direct3d10/d3d10-effect-state-management)
