%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *message);
%}
%token HELLO WORLD
%%
greeting: HELLO ',' WORLD '!' { puts("Hello, World!"); };
%%
int main(void) { return yyparse(); }
void yyerror(const char *message) { fprintf(stderr, "%s\n", message); }
