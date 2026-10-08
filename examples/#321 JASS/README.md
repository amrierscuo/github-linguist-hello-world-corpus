# #321 JASS

Mostrare Hello, World! ai giocatori di una mappa Warcraft III tramite BJDebugMsg.

Tipo canonico `programming`, language_id `504860504`.

Toolchain prevista: pjass per il controllo; Warcraft III con common.j e Blizzard.j per eseguire.

Dalla cartella dell’esempio:

```sh
pjass common.j Blizzard.j hello.j
```

Risultato atteso: script accettato; messaggio Hello, World! visibile nella mappa di prova.

common.j e Blizzard.j appartengono alla toolchain del gioco e non vengono inventati o redistribuiti qui. La semantica richiede la mappa e il runtime Warcraft III.

Stato iniziale: creato; sintassi e semantica in attesa. Librerie JASS del gioco e runtime della mappa non disponibili.

Fonti:

- [pjass — compilatore originale](https://github.com/lep/pjass)
- [GitHub Linguist — esempi JASS](https://github.com/github-linguist/linguist/tree/main/samples/JASS)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.j` | [hello.j](hello.j) creato, verifiche pendenti |
