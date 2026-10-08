#include <stdio.h>
#include <string.h>
%%{
 machine greeting;
 main := "Hello, World!";
}%%
%% write data;
int main(void) {
 const char *p = "Hello, World!", *pe = p + strlen(p);
 int cs;
 %% write init;
 %% write exec;
 if (cs < greeting_first_final || p != pe) return 1;
 puts("Hello, World!");
 return 0;
}
