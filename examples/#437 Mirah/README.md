# #437 Mirah

Compilare Mirah in bytecode JVM e stampare il saluto.

Tipo canonico `programming`, language_id `232`.

Toolchain prevista: Mirah compiler e JVM compatibili.

Dalla cartella dell’esempio:

```sh
mirahc hello.mirah
java Hello
```

Risultato atteso: stdout Hello, World! e newline.

Il sorgente usa la forma Ruby-like Mirah; Ruby da solo non ne verifica il typing o la generazione JVM.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Mirah — guida e compiler](https://github.com/mirah/mirah)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.druby` | [hello.druby](variants/druby-ff72b814/hello.druby) creato, verifiche pendenti |
| `.duby` | [hello.duby](variants/duby-6fa18d7f/hello.duby) creato, verifiche pendenti |
| `.mirah` | [hello.mirah](hello.mirah) creato, verifiche pendenti |
