# #439 Modula-2

Compilare Modula-2 con libreria PIM InOut e stampare il saluto.

Tipo canonico `programming`, language_id `234`.

Toolchain prevista: GNU Modula-2 gm2 con librerie PIM.

Dalla cartella dell’esempio:

```sh
gm2 -fpim Hello.mod -o hello
./hello
```

Risultato atteso: stdout Hello, World! e newline.

La libreria InOut è della famiglia PIM; la toolchain deve usare il dialect corrispondente.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [GNU Modula-2 — manuale](https://gcc.gnu.org/onlinedocs/gm2/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mod` | [Hello.mod](Hello.mod) creato, verifiche pendenti |
