# 0041 Assembly — variante `.i`

Ruolo: Sorgente assembly GNU già privo di macro del preprocessore; .i indica qui l’ingresso testuale preprocessato.

Tipo variante: **alias**. Copia byte-identica di examples/#041 Assembly/hello.s

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
as --64 hello.i -o <output>/hello.o; ld <output>/hello.o -o <output>/hello; <output>/hello
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
