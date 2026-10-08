{ }
rule greeting = parse
  | "Hello, World!" { print_endline "Hello, World!" }
  | _ { failwith "unexpected input" }
{ let () = greeting (Lexing.from_string "Hello, World!") }
