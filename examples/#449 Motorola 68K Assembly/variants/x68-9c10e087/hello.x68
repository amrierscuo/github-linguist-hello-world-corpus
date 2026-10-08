        .text
        .globl _start
_start:
        moveq #4,%d0
        moveq #1,%d1
        lea message,%a0
        move.l %a0,%d2
        moveq #14,%d3
        trap #0
        moveq #1,%d0
        clr.l %d1
        trap #0
        .data
message:
        .ascii "Hello, World!\n"
