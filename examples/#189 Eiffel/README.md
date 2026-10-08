# #189 Eiffel

Compilare una classe root Eiffel e stampare Hello, World! seguito da newline.

Tipo canonico `programming`, language_id `99`.

Toolchain prevista: EiffelStudio con compilatore ec e libreria base.

Dalla cartella dell’esempio:

```sh
Compilare hello_world.e come classe root HELLO_WORLD, creazione make; eseguire il programma prodotto.
```

Risultato atteso: stdout `Hello, World!` seguito da newline.

In Eiffel %N indica il newline dentro una stringa. La configurazione del sistema va creata nell’IDE o con la funzione di compilazione di singolo file documentata per la distribuzione.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [Eiffel — Hello World e compilazione](https://www.eiffel.org/article/hello_world)
- [Eiffel — tutorial del linguaggio](https://www.eiffel.org/doc/eiffel/ET-_Hello_World)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.e` | [hello_world.e](hello_world.e) creato, verifiche pendenti |
