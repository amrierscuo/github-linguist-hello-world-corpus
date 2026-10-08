# 0262 Godot Resource — variante `.gdns`

Ruolo: Descriptor GDNative Godot 3 NativeScript con resource_name Hello, World!, che riferisce una libreria GDNative e la classe Greeting.

Tipo variante: **adapted**. Modello di partenza: examples/#262 Godot Resource/hello.tscn; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Godot 3.5: importare il descriptor; leggere resource_name e controllare il riferimento alla libreria. Per invocare la classe compilare una vera libreria GDNative Greeting esterna. Godot 4 non è il reader di questo formato.
```

Risultato atteso: Descriptor importabile con resource_name Hello, World!; libreria compilata e metodo Greeting ancora da fornire.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html](https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html)
- [https://docs.godotengine.org/en/stable/classes/class_packedscene.html](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [https://github.com/godotengine/godot/releases](https://github.com/godotengine/godot/releases)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.godotengine.org/en/3.5/classes/class_gdnativelibrary.html](https://docs.godotengine.org/en/3.5/classes/class_gdnativelibrary.html)
- [https://docs.godotengine.org/en/3.5/classes/class_nativescript.html](https://docs.godotengine.org/en/3.5/classes/class_nativescript.html)
- [https://github.com/godotengine/godot/blob/3.5-stable/modules/gdnative/gdnative.cpp](https://github.com/godotengine/godot/blob/3.5-stable/modules/gdnative/gdnative.cpp)
