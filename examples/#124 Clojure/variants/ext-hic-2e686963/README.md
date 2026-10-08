# 0124 Clojure — variante `.hic`

Ruolo: Dato Hiccup (vector DOM), non programma Clojure con main.

Tipo variante: **adapted**. Modello di partenza: examples/#124 Clojure/hello.clj; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Clojure/Hiccup: leggere hello.hic con read-string; (hiccup2.core/html dato) e verificare h1.
```

Risultato atteso: <main><h1>Hello, World!</h1></main>

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://clojure.org/reference/repl_and_main](https://clojure.org/reference/repl_and_main)
- [https://clojure.org/reference/special_forms#let](https://clojure.org/reference/special_forms#let)
- [https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/](https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/weavejester/hiccup](https://github.com/weavejester/hiccup)
