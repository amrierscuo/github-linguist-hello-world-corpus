# #598 Raku

Eseguire Raku e stampare il saluto.

Tipo canonico `programming`, language_id `283`.

Toolchain prevista: Rakudo Raku.

Dalla cartella dell’esempio:

```sh
raku hello.raku
```

Risultato atteso: stdout Hello, World! e newline.

Il sorgente richiede Raku; Perl5 non ne verifica il linguaggio.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Rakudo2022.12 + MoarVM2022.12 original runtime. [Log](verification/result.json). 

Fonti:

- [Raku say](https://docs.raku.org/routine/say)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.6pl` | [hello.6pl](variants/6pl-9b762448/hello.6pl) creato, verifiche pendenti |
| `.6pm` | [Greeting.6pm](variants/6pm-9ec874b4/Greeting.6pm) creato, verifiche pendenti |
| `.nqp` | [hello.nqp](variants/nqp-2067113e/hello.nqp) creato, verifiche pendenti |
| `.p6` | [hello.p6](variants/p6-841002fe/hello.p6) creato, verifiche pendenti |
| `.p6l` | [Greeting.p6l](variants/p6l-965ff65c/Greeting.p6l) creato, verifiche pendenti |
| `.p6m` | [Greeting.p6m](variants/p6m-aa906888/Greeting.p6m) creato, verifiche pendenti |
| `.pl` | [hello.pl](variants/pl-b0d52ba4/hello.pl) creato, verifiche pendenti |
| `.pl6` | [hello.pl6](variants/pl6-2abc115e/hello.pl6) creato, verifiche pendenti |
| `.pm` | [Greeting.pm](variants/pm-c810ce30/Greeting.pm) creato, verifiche pendenti |
| `.pm6` | [Greeting.pm6](variants/pm6-537f0d88/Greeting.pm6) creato, verifiche pendenti |
| `.raku` | [hello.raku](hello.raku), [main.raku](variants/6pm-9ec874b4/main.raku), [main.raku](variants/p6l-965ff65c/main.raku), [main.raku](variants/p6m-aa906888/main.raku), [main.raku](variants/pm-c810ce30/main.raku), [main.raku](variants/pm6-537f0d88/main.raku), [main.raku](variants/rakumod-ba1cf06e/main.raku) creato, verifiche pendenti |
| `.rakumod` | [Greeting.rakumod](variants/rakumod-ba1cf06e/Greeting.rakumod) creato, verifiche pendenti |
| `.t` | [hello.t](variants/t-3c247edb/hello.t) creato, verifiche pendenti |
