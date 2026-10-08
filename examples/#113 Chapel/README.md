# #113 Chapel

Compilare un programma Chapel che stampa Hello, World! seguito da LF.

Tipo canonico: `programming`; `language_id`: `55`.

Toolchain prevista: Chapel 2.x, compilatore chpl. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
chpl hello.chpl -o hello
./hello
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

Chapel consente una sequenza di istruzioni a livello del modulo; writeln è disponibile senza import esplicito.

Stato iniziale: artefatto creato, sintassi e semantica in attesa. Toolchain specifica non ancora eseguita su questo esempio; sintassi e semantica restano da verificare.

Fonti primarie o riferimenti originali del progetto:

- [Chapel — primo programma](https://chapel-lang.org/docs/users-guide/base/hello.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.chpl` | [hello.chpl](hello.chpl) creato, verifiche pendenti |
