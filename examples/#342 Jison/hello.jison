%lex
%%
\s+                     /* skip whitespace */
"Hello"                 return 'HELLO';
","                     return 'COMMA';
"World"                 return 'WORLD';
"!"                     return 'BANG';
<<EOF>>                 return 'EOF';
.                       return 'INVALID';
/lex

%start greeting
%%
greeting
  : HELLO COMMA WORLD BANG EOF { return $1 + ", " + $3 + "!"; }
  ;
