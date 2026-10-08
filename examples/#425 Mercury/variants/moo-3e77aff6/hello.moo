:- module hello.
:- interface.

:- type token ---> hello ; eof.
:- parse(greeting/1, token, eof, corpus, in, out).

:- implementation.
:- import_module string.

:- rule greeting(string).
greeting(Text) ---> [hello], { Text = "Hello, World!" }.
