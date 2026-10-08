# #582 R

Eseguire R e stampare il saluto.

Tipo canonico `programming`, language_id `307`.

Toolchain prevista: GNU R Rscript.

Dalla cartella dell’esempio:

```sh
Rscript --vanilla hello.r
```

Risultato atteso: stdout Hello, World! e newline.

cat scrive senza prefisso [1] e senza virgolette.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: GNU R 4.3.3 native Ubuntu runtime. [Log](verification/result.json). 

Fonti:

- [R introduction](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.r` | [hello.r](hello.r) verificato |
| `.rd` | [hello.rd](variants/rd-0443eb91/hello.rd) creato, verifiche pendenti |
| `.rhistory` | [hello.rhistory](variants/rhistory-375f1003/hello.rhistory) creato, verifiche pendenti |
| `.rsx` | [hello.rsx](variants/rsx-7f28a360/hello.rsx) creato, verifiche pendenti |
