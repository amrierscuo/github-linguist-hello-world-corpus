%%
\s+                     /* skip whitespace */
"Hello"                 return 'HELLO';
","                     return 'COMMA';
"World"                 return 'WORLD';
"!"                     return 'BANG';
<<EOF>>                 return 'EOF';
.                       return 'INVALID';
