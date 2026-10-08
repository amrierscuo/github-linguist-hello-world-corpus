.equ CORPUS_WRITE, 1
.equ CORPUS_EXIT, 60
.section .rodata
corpus_message: .ascii "Hello, World!\n"
.equ corpus_message_length, . - corpus_message
