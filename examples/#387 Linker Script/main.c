#include <stdio.h>
#include <stddef.h>
__attribute__((section(".greeting"), used))
static const char greeting[] = "Hello, World!";
extern const char __greeting_start[], __greeting_end[];
int main(void) {
    if (__greeting_end - __greeting_start != 14) return 1;
    puts(__greeting_start);
    return 0;
}
