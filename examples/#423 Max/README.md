# #423 Max

Aprire un patch Max e inviare il saluto al print object cliccando il message box.

Tipo canonico `programming`, language_id `227`.

Toolchain prevista: Cycling ’74 Max 8+.

Dalla cartella dell’esempio:

```sh
Aprire hello.maxpat; cliccare il message box e leggere la Max Console.
```

Risultato atteso: patch accettato; console contiene greeting: Hello, World!.

Non produce audio: è un patch di messaggi con una connessione. Un generico parser JSON non valida il namespace o l’esecuzione Max.

Stato iniziale: creato; sintassi e semantica in attesa. Runtime Max non disponibile.

Fonti:

- [Cycling ’74 — message](https://docs.cycling74.com/reference/message/)
- [Cycling ’74 — print](https://docs.cycling74.com/reference/print/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.maxpat` | [hello.maxpat](hello.maxpat), [hello.maxpat](variants/maxproj-b699244e/hello.maxpat) creato, verifiche pendenti |
| `.maxhelp` | [hello.maxhelp](variants/maxhelp-2204353b/hello.maxhelp) creato, verifiche pendenti |
| `.maxproj` | [hello.maxproj](variants/maxproj-b699244e/hello.maxproj) creato, verifiche pendenti |
| `.mxt` | [hello.mxt](variants/mxt-8fccfadd/hello.mxt) creato, verifiche pendenti |
| `.pat` | [hello.pat](variants/pat-b636baf1/hello.pat) creato, verifiche pendenti |
