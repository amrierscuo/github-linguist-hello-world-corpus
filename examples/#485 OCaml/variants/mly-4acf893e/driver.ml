let () =
  let tokens = ref [Hello.HELLO; Hello.EOF] in
  let lexer _ = match !tokens with
    | t :: rest -> tokens := rest; t
    | [] -> Hello.EOF
  in print_endline (Hello.greeting lexer (Lexing.from_string ""))
