%option noyywrap nodefault
%{
#include <stdio.h>
%}
%%
hello      { puts("Hello, World!"); }
[ \t\r\n]+  ;
.          { fprintf(stderr, "Unexpected input: %s\n", yytext); return 1; }
%%
int main(void) { return yylex(); }
