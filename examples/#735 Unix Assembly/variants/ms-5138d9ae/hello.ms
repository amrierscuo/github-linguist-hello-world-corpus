.section .rodata
greeting: .ascii "Hello, World!\n"
.set greeting_length, .-greeting
.section .text
.global _start
_start:
 mov $1, %rax
 mov $1, %rdi
 lea greeting(%rip), %rsi
 mov $greeting_length, %rdx
 syscall
 mov $60, %rax
 xor %rdi, %rdi
 syscall
