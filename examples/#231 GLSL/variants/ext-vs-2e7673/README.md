# 0231 GLSL — variante `.vs`

Ruolo: Shader GLSL dello stadio vert con payload numerico dei code point, non fragment rinominato.

Tipo variante: **adapted**. Modello di partenza: examples/#231 GLSL/hello.frag; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
glslangValidator -V --target-env vulkan1.2 -S vert hello.vs -o <output>/hello.spv; spirv-val --target-env vulkan1.2 <output>/hello.spv; pipeline GPU dello stadio vert per leggere 13 valori.
```

Risultato atteso: Compilazione e validazione SPIR-V dello stadio; pipeline eseguita restituisce i 13 code point del saluto.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/KhronosGroup/glslang](https://github.com/KhronosGroup/glslang)
- [https://github.com/KhronosGroup/SPIRV-Tools](https://github.com/KhronosGroup/SPIRV-Tools)
- [https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.50.pdf)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.60.pdf](https://registry.khronos.org/OpenGL/specs/gl/GLSLangSpec.4.60.pdf)
- [https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_tracing.txt](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_tracing.txt)
