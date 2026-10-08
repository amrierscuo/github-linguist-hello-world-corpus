%token HELLO EOF
%start greeting
%type <string> greeting
%%
greeting: HELLO EOF { "Hello, World!" };
