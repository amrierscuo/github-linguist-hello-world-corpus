# 0262 Godot Resource — variante `.tres`

Ruolo: Risorsa Godot 4 con property esportata dal Resource script, non PackedScene tscn rinominata.

Tipo variante: **adapted**. Modello di partenza: examples/#262 Godot Resource/hello.tscn; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Godot 4 nel progetto temporaneo: ResourceLoader.load("res://hello.tres"); confrontare resource.message.
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

- [https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html](https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html)
- [https://docs.godotengine.org/en/stable/classes/class_packedscene.html](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [https://github.com/godotengine/godot/releases](https://github.com/godotengine/godot/releases)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html](https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html)
