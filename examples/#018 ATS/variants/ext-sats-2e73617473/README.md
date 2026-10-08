# 0018 ATS — variante `.sats`

Ruolo: Firma statica ATS; il companion implementa la funzione dichiarata.

Tipo variante: **adapted**. Modello di partenza: examples/#018 ATS/hello.dats; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
patscc -DATS_MEMALLOC_LIBC consumer.dats -o <output>/hello; <output>/hello
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

- [https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html](https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html)
- [https://github.com/githwxi/ATS-Postiats](https://github.com/githwxi/ATS-Postiats)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c235.html](https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c235.html)
