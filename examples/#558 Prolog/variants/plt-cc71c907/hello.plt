:- begin_tests(corpus_greeting).
test(greeting) :-
    atom_concat('Hello, ', 'World!', Greeting),
    assertion(Greeting == 'Hello, World!').
:- end_tests(corpus_greeting).
