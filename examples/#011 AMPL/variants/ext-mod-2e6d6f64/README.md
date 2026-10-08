# 0011 AMPL — variante `.mod`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#011 AMPL/hello.ampl

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
ampl hello.mod
```

Risultato atteso: Exit 0; stderr vuoto; stdout esattamente Hello, World! e un terminatore LF/CRLF (CRLF osservato su Windows).

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)
- [https://dev.ampl.com/ampl/python/index.html](https://dev.ampl.com/ampl/python/index.html)
- [https://pypi.ampl.com/ampl-module-base/](https://pypi.ampl.com/ampl-module-base/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
