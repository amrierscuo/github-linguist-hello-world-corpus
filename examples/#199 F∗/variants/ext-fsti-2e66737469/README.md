# 0199 F* — variante `.fsti`

Ruolo: Firma F* della funzione main, con implementazione FST omonima.

Tipo variante: **adapted**. Modello di partenza: examples/#199 F∗/Hello.fst; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
F* originale: typecheck Hello.fsti e Hello.fst; estrarre e invocare Hello.main().
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

- [https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html](https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html)
- [https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti](https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://fstar-lang.org/tutorial/book/part1/part1_modules.html](https://fstar-lang.org/tutorial/book/part1/part1_modules.html)
