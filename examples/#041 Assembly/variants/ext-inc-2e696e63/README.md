# 0041 Assembly — variante `.inc`

Ruolo: Include GNU assembler x86-64 con simboli e dati; il consumer richiama write/exit.

Tipo variante: **adapted**. Modello di partenza: examples/#041 Assembly/hello.s; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
as --64 consumer.s -o <output>/hello.o; ld <output>/hello.o -o <output>/hello; <output>/hello
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

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
