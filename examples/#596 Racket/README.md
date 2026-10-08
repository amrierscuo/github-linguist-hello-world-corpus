# #596 Racket

Eseguire un modulo Racket e stampare il saluto.

Tipo canonico `programming`, language_id `316`.

Toolchain prevista: Racket.

Dalla cartella dell’esempio:

```sh
racket hello.rkt
```

Risultato atteso: stdout Hello, World! e newline.

Modulo base senza dipendenze esterne.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Racket 8.18 native Windows portable. [Log](verification/result.json). 

Fonti:

- [Racket displayln](https://docs.racket-lang.org/reference/Writing.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rkt` | [hello.rkt](hello.rkt) verificato |
| `.rktd` | [hello.rktd](variants/rktd-18ea1173/hello.rktd) creato, verifiche pendenti |
| `.rktl` | [hello.rktl](variants/rktl-c9a39abc/hello.rktl) creato, verifiche pendenti |
| `.scrbl` | [hello.scrbl](variants/scrbl-ba477af2/hello.scrbl) creato, verifiche pendenti |
