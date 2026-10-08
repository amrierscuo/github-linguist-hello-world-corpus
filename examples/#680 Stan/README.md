# #680 Stan

Compilare un modello Stan che stampa il saluto nella fase transformed data.

Tipo canonico `programming`, language_id `356`.

Toolchain prevista: Stan stanc compiler e CmdStan runtime.

Dalla cartella dell’esempio:

```sh
stanc hello.stan --o=build/hello.hpp
```

Risultato atteso: modello compilato; l’inizializzazione CmdStan stampa Hello, World!.

Il print dipende dal runtime: il C++ generato dal compiler da solo prova la sintassi.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Stan print](https://mc-stan.org/docs/reference-manual/statements.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.stan` | [hello.stan](hello.stan) creato, verifiche pendenti |
