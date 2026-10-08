# Kotlin .ktm

Sorgente Kotlin testuale, alias byte identico del campione principale.
Il detector ufficiale Vim 9.0.0000 associa *.kt, *.ktm e *.kts al filetype kotlin.
Questa associazione non prova che kotlinc moderno accetti direttamente .ktm.

## Procedura

Copiare hello.ktm in una directory di build esterna come Hello.kt; compilare con kotlinc Hello.kt -include-runtime -d hello.jar; eseguire java -jar hello.jar. Il caricamento diretto del suffisso .ktm nel compilatore moderno resta da verificare.

Risultato atteso: Hello, World! e newline.
Sintassi e semantica della variante restano da verificare.

## Fonti

https://raw.githubusercontent.com/vim/vim/v9.0.0000/runtime/filetype.vim
https://kotlinlang.org/docs/command-line.html
