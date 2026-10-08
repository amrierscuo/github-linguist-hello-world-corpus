# #669 Smali

Assemblare Smali in DEX con un metodo main che stampa il saluto.

Tipo canonico `programming`, language_id `351`.

Toolchain prevista: Google smali assembler e Android ART/Dalvik per esecuzione.

Dalla cartella dell’esempio:

```sh
smali assemble Hello.smali -o build/hello.dex
```

Risultato atteso: DEX valido; main stampa Hello, World! sul runtime Android.

Assemblare il DEX non prova l’esecuzione ART; questa resta distinta.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Smali](https://github.com/google/smali)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.smali` | [Hello.smali](Hello.smali) creato, verifiche pendenti |
