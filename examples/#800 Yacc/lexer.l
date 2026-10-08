%option noyywrap
%{
#include "hello.tab.h"
%}
%%
"Hello" return HELLO;
"World" return WORLD;
[ \t\r\n]+ ;
. return (unsigned char)yytext[0];
%%
