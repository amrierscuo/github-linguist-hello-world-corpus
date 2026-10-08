# #427 Meson

Configurare un progetto Meson e lanciare un run_target che stampa il saluto.

Tipo canonico `programming`, language_id `799141244`.

Toolchain prevista: Meson, Ninja e Python 3.13.

Dalla cartella dell’esempio:

```sh
meson setup build
meson compile -C build hello
```

Risultato atteso: target hello eseguito con successo; stdout contiene una riga Hello, World!.

Il progetto non richiede un compilatore C: Meson interpreta la ricetta e Ninja esegue il target Python.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + Meson 1.12.1 + Ninja 1.13.2. [Log](verification/result.json). 

Fonti:

- [Meson — run targets](https://mesonbuild.com/Run-targets.html)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install meson==1.12.1 ninja==1.13.2
```
