# 0231 GLSL — variante `.glsl`

Ruolo: Shader fragment GLSL; il ruolo frag è specificato nel comando perché il suffisso può essere generico.

Tipo variante: **alias**. Copia byte-identica di examples/#231 GLSL/hello.frag

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
glslangValidator -V -S frag hello.glsl -o <output>/hello.spv; spirv-val <output>/hello.spv
```

Risultato atteso: Compilazione e validazione SPIR-V exit 0; rendering atteso: valori RGB uguali ai 13 byte ASCII divisi per 255.

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
