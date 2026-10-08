%%
%public
%class GreetingLexer
%standalone
%unicode
%%
World { System.out.println("Hello, World!"); }
[ \t\r\n]+ { /* whitespace */ }
