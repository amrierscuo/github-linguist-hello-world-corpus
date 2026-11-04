# 0262 Godot Resource: variant `.gdns`

Role: Descriptor GDNative Godot 3 NativeScript with resource_name Hello, World!, which reports a GDNative library and the Greeting class.

Version type: **adapted**. Starting model: examples/#262 Godot Resource/hello.tscn; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Godot 3.5: importare il descriptor; leggere resource_name e controllare il riferimento alla libreria. Per invocare la classe compilare una vera libreria GDNative Greeting esterna. Godot 4 non è il reader di questo formato.
```

Expected result: Importable descriptor with resource_name Hello, World!; compiled library and Greeting method still to be supplied.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html](https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html)
- [https://docs.godotengine.org/en/stable/classes/class_packedscene.html](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [https://github.com/godotengine/godot/releases](https://github.com/godotengine/godot/releases)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.godotengine.org/en/3.5/classes/class_gdnativelibrary.html](https://docs.godotengine.org/en/3.5/classes/class_gdnativelibrary.html)
- [https://docs.godotengine.org/en/3.5/classes/class_nativescript.html](https://docs.godotengine.org/en/3.5/classes/class_nativescript.html)
- [https://github.com/godotengine/godot/blob/3.5-stable/modules/gdnative/gdnative.cpp](https://github.com/godotengine/godot/blob/3.5-stable/modules/gdnative/gdnative.cpp)
