.intel_syntax noprefix
.section .rodata
message:
    .ascii "Hello, World!\n"
.equ message_length, . - message

.section .text
.global _start
_start:
    mov eax, 1
    mov edi, 1
    lea rsi, [rip + message]
    mov edx, message_length
    syscall
    mov eax, 60
    xor edi, edi
    syscall
.section .note.GNU-stack,"",@progbits
