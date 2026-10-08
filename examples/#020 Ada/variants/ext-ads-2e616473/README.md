# 0020 Ada — variante `.ads`

Ruolo: Specificazione di package Ada con costante pubblica, consumata dal programma companion.

Tipo variante: **adapted**. Modello di partenza: examples/#020 Ada/hello.adb; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gnatmake consumer.adb -D <output>; <output>/consumer
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

- [https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
- [https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.adacore.com/live/wave/arm05/html/arm05/RM-7-1.html](https://docs.adacore.com/live/wave/arm05/html/arm05/RM-7-1.html)
