# 0264 Gosu — variante `.gst`

Ruolo: Template Gosu con parametro String, non classe gs.

Tipo variante: **adapted**. Modello di partenza: examples/#264 Gosu/Hello.gs; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Gosu template renderer: caricare hello.gst e renderizzare con name="World".
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

- [https://gosu-lang.github.io/quickstart.html](https://gosu-lang.github.io/quickstart.html)
- [https://github.com/gosu-lang/gosu-lang](https://github.com/gosu-lang/gosu-lang)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://gosu-lang.github.io/docs.html](https://gosu-lang.github.io/docs.html)
