# 0131 ColdFusion — variante `.cfml`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#131 ColdFusion/hello.cfm

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Server CFML isolato: GET /hello.cfml e confrontare il body con il modello.
```

Risultato atteso: HTTP 200; risposta text/plain contenente Hello, World!, senza debug output.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://docs.lucee.org/reference/tags/output.html](https://docs.lucee.org/reference/tags/output.html)
- [https://docs.lucee.org/reference/tags/content.html](https://docs.lucee.org/reference/tags/content.html)
- [https://docs.lucee.org/reference/tags/setting.html](https://docs.lucee.org/reference/tags/setting.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
