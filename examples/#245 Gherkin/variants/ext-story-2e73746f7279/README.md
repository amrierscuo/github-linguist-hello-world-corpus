# 0245 Gherkin — variante `.story`

Ruolo: Story JBehave (Scenario/Given/When/Then), distinto dall’header Feature di Gherkin feature.

Tipo variante: **adapted**. Modello di partenza: examples/#245 Gherkin/hello.feature; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
JBehave StoryParser: leggere hello.story e collegare step bindings del progetto di test temporaneo.
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

- [https://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/)
- [https://github.com/cucumber/cucumber-js](https://github.com/cucumber/cucumber-js)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://jbehave.org/reference/stable/story-syntax.html](https://jbehave.org/reference/stable/story-syntax.html)
