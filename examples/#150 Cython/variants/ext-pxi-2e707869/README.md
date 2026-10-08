# 0150 Cython — variante `.pxi`

Ruolo: Include Cython pxi, incluso testualmente nella unità companion.

Tipo variante: **adapted**. Modello di partenza: examples/#150 Cython/hello.pyx; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Cython/setuptools: compilare consumer.pyx; python -c "import consumer"
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

- [https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html](https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html)
- [https://github.com/cython/cython](https://github.com/cython/cython)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html](https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html)
