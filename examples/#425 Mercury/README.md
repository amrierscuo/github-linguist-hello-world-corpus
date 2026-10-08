# #425 Mercury

Compilare un programma Mercury deterministico con io state threading.

Tipo canonico `programming`, language_id `229`.

Toolchain prevista: Mercury mmc e grade runtime installata.

Dalla cartella dell’esempio:

```sh
mmc --make hello
./hello
```

Risultato atteso: stdout Hello, World! e LF, exit 0.

main dichiara determinismo det e usa !IO per passare lo stato di I/O.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Mercury — programma hello](https://www.mercurylang.org/information/doc-latest/mercury_user_guide/Hello-world.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.m` | [hello.m](hello.m) creato, verifiche pendenti |
| `.moo` | [hello.moo](variants/moo-3e77aff6/hello.moo) creato, verifiche pendenti |
