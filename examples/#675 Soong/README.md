# #675 Soong

Interpretare un modulo genrule Soong che genera un file di saluto.

Tipo canonico `data`, language_id `222900098`.

Toolchain prevista: AOSP Soong build system.

Dalla cartella dell’esempio:

```sh
m corpus_hello_world
```

Risultato atteso: output del genrule contiene Hello, World! e newline.

Non è JSON o un generico HCL: richiede il modello Blueprint/Soong.

Stato iniziale: creato; sintassi e semantica in attesa. Checkout AOSP/Soong di prova non disponibile.

Fonti:

- [Soong](https://android.googlesource.com/platform/build/soong/+/refs/heads/main/README.md)
