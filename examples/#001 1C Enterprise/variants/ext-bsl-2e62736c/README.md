# 0001 1C Enterprise — variante `.bsl`

Ruolo: Modulo sorgente BSL 1C/OneScript: stessa istruzione Сообщить del modello .os; il reader/runtime va invocato esplicitamente sul file BSL.

Tipo variante: **alias**. Copia byte-identica di examples/#001 1C Enterprise/hello.os

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
oscript hello.bsl
```

Risultato atteso: Syntax check: exit 0, No errors.; run: exit 0, exactly Hello, World! followed by newline

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.oscript.io/](https://www.oscript.io/)
- [https://www.oscript.io/learn/tutorial-info](https://www.oscript.io/learn/tutorial-info)
- [https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0](https://github.com/EvilBeaver/OneScript/releases/tag/v2.2.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
