# 0218 FreeBASIC — variante `.bi`

Ruolo: Include FreeBASIC bi con funzione, incluso dal programma companion.

Tipo variante: **adapted**. Modello di partenza: examples/#218 FreeBASIC/hello.bas; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
fbc consumer.bas -x <output>/hello; <output>/hello
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

- [https://www.freebasic.net/wiki/KeyPgPrint](https://www.freebasic.net/wiki/KeyPgPrint)
- [https://www.freebasic.net/wiki/KeyPgString](https://www.freebasic.net/wiki/KeyPgString)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.freebasic.net/wiki/KeyPgInclude](https://www.freebasic.net/wiki/KeyPgInclude)
