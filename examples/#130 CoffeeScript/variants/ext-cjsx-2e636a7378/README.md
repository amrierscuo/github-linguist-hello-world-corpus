# 0130 CoffeeScript — variante `.cjsx`

Ruolo: Componente JSX in CoffeeScript, richiede frontend CJSX prima di CoffeeScript.

Tipo variante: **adapted**. Modello di partenza: examples/#130 CoffeeScript/hello.coffee; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
coffee-react-transform hello.cjsx > <output>/hello.coffee; coffee -c -o <output> <output>/hello.coffee; node <output>/hello.js
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

- [https://coffeescript.org/#installation](https://coffeescript.org/#installation)
- [https://coffeescript.org/#strings](https://coffeescript.org/#strings)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/jsdf/coffee-react-transform](https://github.com/jsdf/coffee-react-transform)
