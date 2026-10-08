bits 64
global _start
section .rodata
message: db "Hello, World!",10
length: equ $-message
section .text
_start:
 mov eax,1
 mov edi,1
 lea rsi,[rel message]
 mov edx,length
 syscall
 mov eax,60
 xor edi,edi
 syscall
