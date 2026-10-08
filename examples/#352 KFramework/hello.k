module HELLO
  imports STRING
  syntax KItem ::= "hello"
  configuration <k> $PGM:K </k>
  rule <k> hello => "Hello, World!" ... </k>
endmodule
