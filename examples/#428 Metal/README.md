# #428 Metal

Compilare un kernel Metal che scrive i 13 byte del saluto in un buffer.

Tipo canonico `programming`, language_id `230`.

Toolchain prevista: macOS Xcode Metal compiler e Metal runtime.

Dalla cartella dell’esempio:

```sh
xcrun -sdk macosx metal -c hello.metal -o build/hello.air
```

Risultato atteso: kernel compilato; dispatch di 13 thread produce bytes ASCII Hello, World!.

La semantica richiede anche un host Metal con buffer e dispatch; la compilazione da sola non viene contata come esecuzione.

Stato iniziale: creato; sintassi e semantica in attesa. Xcode e runtime Metal non disponibili su Windows.

Fonti:

- [Apple — Metal Shading Language specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.metal` | [hello.metal](hello.metal) creato, verifiche pendenti |
