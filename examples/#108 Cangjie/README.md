# #108 Cangjie

Compilare un programma Cangjie che stampa Hello, World! seguito da newline.

Tipo canonico: `programming`; `language_id`: `581895317`.

Toolchain prevista: Cangjie SDK 1.0.0 o compatibile, compilatore cjc. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
cjc hello.cj -o hello
./hello
```

Risultato atteso: stdout `Hello, World!` seguito da newline, uscita 0.

Su Windows produrre hello.exe e avviarlo con .\hello.exe. La firma main e println seguono la guida del compilatore.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Cangjie — primo programma](https://docs.cangjie-lang.cn/en/docs/1.0.0/user_manual/source_en/first_understanding/hello_world.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cj` | [hello.cj](hello.cj) creato, verifiche pendenti |
