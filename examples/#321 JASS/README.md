# #321 JASS

Show Hello, World! to players of a map Warcraft III via BJDebugMsg.

Canonical type `programming`, language_id `504860504`.

Suggested toolchain: pjass for control; Warcraft III with common.j and Blizzard.j to perform.

From the example directory:

```sh
pjass common.j Blizzard.j hello.j
```

Expected result: accepted script; Hello, World! message visible in the test map.

common.j e Blizzard.j appartengono alla toolchain del gioco e non vengono inventati o redistribuiti qui. La semantica richiede la mappa e il runtime Warcraft III.

Stato iniziale: creato; sintassi e semantica in attesa. Librerie JASS del gioco e runtime della mappa non disponibili.

Sources:

- [pjass — compilatore originale](https://github.com/lep/pjass)
- [GitHub Linguist — esempi JASS](https://github.com/github-linguist/linguist/tree/main/samples/JASS)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.j` | [hello.j](hello.j) created; verification pending |
