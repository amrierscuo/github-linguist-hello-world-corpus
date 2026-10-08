:- initialization(main, main).

main :-
    atomic_list_concat(['Hello, ', 'World!'], Greeting),
    writeln(Greeting).
