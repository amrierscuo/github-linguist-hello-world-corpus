# 0272 Groovy — variante `.grt`

Ruolo: Template Groovy GStringTemplateEngine, distinto da uno script console .groovy.

Tipo variante: **adapted**. Modello di partenza: examples/#272 Groovy/hello.groovy; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
groovy render.groovy
```

Risultato atteso: Hello, World!

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://groovy-lang.org/syntax.html#_string_interpolation](https://groovy-lang.org/syntax.html#_string_interpolation)
- [https://groovy-lang.org/](https://groovy-lang.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.groovy-lang.org/latest/html/documentation/template-engines.html](https://docs.groovy-lang.org/latest/html/documentation/template-engines.html)
