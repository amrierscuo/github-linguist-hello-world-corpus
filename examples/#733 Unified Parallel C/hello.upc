#include <stdio.h>
#include <upc.h>
int main(void) { if (MYTHREAD == 0) puts("Hello, World!"); upc_barrier; return 0; }
