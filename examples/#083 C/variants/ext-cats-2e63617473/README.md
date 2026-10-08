# 0083 C — variante `.cats`

Ruolo: Codice C incorporabile dal FFI ATS; file .cats con grammatica C, non sorgente ATS.

Tipo variante: **alias**. Copia byte-identica di examples/#083 C/hello.c

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gcc -x c hello.cats -o <output>/hello; <output>/hello
```

Risultato atteso: Compilazione exit 0; programma exit 0 e stdout Hello, World! più newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html](https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
