#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <rpc/rpc.h>
#include "hello.h"
int main(void) {
 char buffer[256]; greeting input = "Hello, World!", output = NULL;
 XDR stream; xdrmem_create(&stream, buffer, sizeof buffer, XDR_ENCODE);
 assert(xdr_greeting(&stream, &input)); u_int length=xdr_getpos(&stream); xdr_destroy(&stream);
 xdrmem_create(&stream, buffer, length, XDR_DECODE);
 assert(xdr_greeting(&stream, &output)); assert(strcmp(output, "Hello, World!")==0);
 puts(output); xdr_destroy(&stream); xdr_free((xdrproc_t)xdr_greeting, (char *)&output); return 0;
}
