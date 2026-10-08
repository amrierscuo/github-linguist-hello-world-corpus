package Hello;
(* synthesize *)
module mkHello(Empty);
  rule sayGreeting;
    $display("Hello, World!");
    $finish(0);
  endrule
endmodule
endpackage
