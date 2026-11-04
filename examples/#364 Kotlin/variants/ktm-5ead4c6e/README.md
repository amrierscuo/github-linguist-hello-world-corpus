# Kotlin .ktm

Source textual Kotlin, alias byte identical to the main sample.
The official Vim 9.0.0000 detector associates * .kt, * .ktm and * .kts to the kotlin filetype.
This association does not prove that modern kotlinc accepts directly .ktm.

## Procedure

Copy hello.ktm in an external build directory such as Hello.kt; fill in with kotlinc Hello.kt -include-runtime -d hello.jar; run java -jar hello.jar. Direct loading of the .ktm suffix in the modern compiler remains to be checked.

Expected result: Hello, World! and newline.
syntax and behavior of the variant remain to be checked.

## Sources

https://raw.githubusercontent.com/vim/vim/v9.0.0000/runtime/filetype.vim
https://kotlinlang.org/docs/command-line.html
