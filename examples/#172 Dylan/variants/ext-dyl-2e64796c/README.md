# 0172 Dylan — variante `.dyl`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#172 Dylan/hello.dylan

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Open Dylan: nel progetto temporaneo del modello indirizzare hello.lid al sorgente hello.dyl; dylan-compiler -build hello.lid; eseguire il binario esterno.
```

Risultato atteso: Compilazione e linking exit 0; eseguibile stampa il saluto più newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://opendylan.org/getting-started-cli/hello-world.html](https://opendylan.org/getting-started-cli/hello-world.html)
- [https://opendylan.org/library-reference/io/format-out.html](https://opendylan.org/library-reference/io/format-out.html)
- [https://opendylan.org/download/index.html](https://opendylan.org/download/index.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
