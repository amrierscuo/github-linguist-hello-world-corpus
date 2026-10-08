# 0133 Common Lisp — variante `.asd`

Ruolo: Descrizione sistema ASDF con componente Lisp che emette il saluto.

Tipo variante: **adapted**. Modello di partenza: examples/#133 Common Lisp/hello.lisp; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
SBCL: require asdf; asdf:load-asd sul file hello.asd; asdf:load-system "corpus-greeting".
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

- [https://www.sbcl.org/manual/#Shebang-Scripts](https://www.sbcl.org/manual/#Shebang-Scripts)
- [https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm](https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm)
- [https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm](https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://asdf.common-lisp.dev/asdf/Defining-systems-with-defsystem.html](https://asdf.common-lisp.dev/asdf/Defining-systems-with-defsystem.html)
