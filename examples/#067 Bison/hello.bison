%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *message);
%}
%start greeting
%%
greeting: %empty { puts("Hello, World!"); };
%%
int yylex(void) { return 0; }
void yyerror(const char *message) { fprintf(stderr, "%s\n", message); }
int main(void) { return yyparse(); }
