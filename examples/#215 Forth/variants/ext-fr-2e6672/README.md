# 0215 Forth — variante `.fr`

Ruolo: Sorgente Forth testuale; .f/.for/.fs in questa cartella non sono sorgenti Fortran o F#.

Tipo variante: **alias**. Copia byte-identica di examples/#215 Forth/hello.fth

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gforth hello.fr
```

Risultato atteso: Exit 0; saluto esatto seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/](https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/)
- [https://forth-standard.org/standard/core/Dotp](https://forth-standard.org/standard/core/Dotp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
