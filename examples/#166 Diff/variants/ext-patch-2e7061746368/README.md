# 0166 Diff — variante `.patch`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#166 Diff/hello.diff

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
GNU patch --dry-run -p1 -d <copia-fixture-originale> < hello.patch; applicare alla copia e leggere il saluto.
```

Risultato atteso: diff exit 1 perché esistono differenze; patch exit 0; file risultante uguale a after/hello.txt.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html](https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html)
- [https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html](https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
