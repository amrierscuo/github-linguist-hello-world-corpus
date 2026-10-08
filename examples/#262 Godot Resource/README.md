# #262 Godot Resource

Voce canonica `Godot Resource`, tipo `data`, language_id `738107771`.

Caricare una scena testuale Godot con un nodo Label e verificare il suo testo dopo istanziazione.

## Toolchain e riproduzione

Official Godot PackedScene loader and engine — 4.7.2.stable.official.ed1daf0bf. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Godot ufficiale 4.7.2 stable Windows x64. Eseguire in una copia di lavoro con project.godot, hello.tscn e verify.gd: Godot può creare cache .godot e metadati accanto al progetto.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
godot --headless --path . --script verify.gd
```

Risultato atteso: Hello, World! e PASS: genuine PackedScene loader and Label.text.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova usa il vero PackedScene loader e confronta Label.text con il saluto. L’ambito semantico è il caricamento della scena e il valore del widget istanziato; non viene dichiarata una verifica visiva dei pixel.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html](https://docs.godotengine.org/en/stable/contributing/development/file_formats/tscn.html)
- [https://docs.godotengine.org/en/stable/classes/class_packedscene.html](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [https://github.com/godotengine/godot/releases](https://github.com/godotengine/godot/releases)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gdnlib` | [hello.gdnlib](variants/ext-gdnlib-2e67646e6c6962/hello.gdnlib) creato, verifiche pendenti |
| `.gdns` | [hello.gdns](variants/ext-gdns-2e67646e73/hello.gdns) creato, verifiche pendenti |
| `.tres` | [hello.tres](variants/ext-tres-2e74726573/hello.tres) creato, verifiche pendenti |
| `.tscn` | [hello.tscn](hello.tscn) verificato |
