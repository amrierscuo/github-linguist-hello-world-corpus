# #440 Modula-3

Compilare Modula-3 con IO e un programma Main.

Tipo canonico `programming`, language_id `564743864`.

Toolchain prevista: Critical Mass Modula-3 cm3 e libm3.

Dalla cartella dell’esempio:

```sh
cm3
Eseguire l’eseguibile hello della directory target generata da cm3.
```

Risultato atteso: stdout Hello, World! e newline.

EXPORTS Main rende il modulo il punto d’ingresso del programma.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [CM3 — repository originale](https://github.com/modula3/cm3)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.i3` | [Greeting.i3](variants/i3-5aa7c7e3/Greeting.i3) creato, verifiche pendenti |
| `.ig` | [Greeting.ig](variants/ig-bbf774c6/Greeting.ig) creato, verifiche pendenti |
| `.m3` | [Hello.m3](Hello.m3), [Greeting.m3](variants/i3-5aa7c7e3/Greeting.m3), [Main.m3](variants/i3-5aa7c7e3/Main.m3), [TextGreeting.m3](variants/ig-bbf774c6/TextGreeting.m3), [Main.m3](variants/ig-bbf774c6/Main.m3), [TextGreeting.m3](variants/mg-63058c94/TextGreeting.m3), [Main.m3](variants/mg-63058c94/Main.m3) creato, verifiche pendenti |
| `.mg` | [Greeting.mg](variants/mg-63058c94/Greeting.mg) creato, verifiche pendenti |
