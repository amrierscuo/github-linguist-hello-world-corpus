corpus_greeting:
        moveq #4,%d0
        moveq #1,%d1
        lea corpus_message,%a0
        move.l %a0,%d2
        moveq #14,%d3
        trap #0
        rts
corpus_message:
        .ascii "Hello, World!\n"
