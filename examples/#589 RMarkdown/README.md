# #589 RMarkdown

Eseguire un chunk R Markdown e renderizzare il saluto in HTML.

Tipo canonico `prose`, language_id `313`.

Toolchain prevista: R, rmarkdown, knitr e Pandoc.

Dalla cartella dell’esempio:

```sh
Rscript -e "rmarkdown::render('hello.rmd')"
```

Risultato atteso: documento HTML con saluto prodotto dal chunk R.

Un parser Markdown da solo non prova l’esecuzione del chunk.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [R Markdown](https://rmarkdown.rstudio.com/lesson-1.html)
- [knitr](https://yihui.org/knitr/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qmd` | [hello.qmd](variants/qmd-6ffe4344/hello.qmd) creato, verifiche pendenti |
| `.rmd` | [hello.rmd](hello.rmd) creato, verifiche pendenti |
