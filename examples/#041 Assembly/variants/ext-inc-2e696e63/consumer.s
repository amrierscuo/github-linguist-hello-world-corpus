.intel_syntax noprefix
.include "hello.inc"
.text
.global _start
_start:
 mov eax,CORPUS_WRITE
 mov edi,1
 lea rsi,[rip+corpus_message]
 mov edx,corpus_message_length
 syscall
 mov eax,CORPUS_EXIT
 xor edi,edi
 syscall
.section .note.GNU-stack,"",@progbits
