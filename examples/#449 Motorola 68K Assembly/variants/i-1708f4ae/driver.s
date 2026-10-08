.text
.globl _start
_start:
        bsr corpus_greeting
        moveq #1,%d0
        clr.l %d1
        trap #0
.include "hello.i"
