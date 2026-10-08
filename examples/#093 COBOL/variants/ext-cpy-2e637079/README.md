# 0093 COBOL — variante `.cpy`

Ruolo: Copybook COBOL di Working-Storage, incluso da COPY.

Tipo variante: **adapted**. Modello di partenza: examples/#093 COBOL/hello.cob; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
cobc -x -free consumer.cob -o <output>/hello; <output>/hello
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

- [https://gnucobol.sourceforge.io/doc/gnucobol.html](https://gnucobol.sourceforge.io/doc/gnucobol.html)
- [https://gnucobol.sourceforge.io/HTML/gnucobpg.html](https://gnucobol.sourceforge.io/HTML/gnucobpg.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://gnucobol.sourceforge.io/](https://gnucobol.sourceforge.io/)
