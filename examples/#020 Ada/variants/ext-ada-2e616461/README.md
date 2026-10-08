# 0020 Ada — variante `.ada`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#020 Ada/hello.adb

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gcc -c -x ada hello.ada -o <output>/hello.o; gnatbind/gnatlink sull’unità Hello nella directory output.
```

Risultato atteso: stdout: Hello World seguito da un a capo; exit 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
- [https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
