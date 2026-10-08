module hello;
  string name = "World";
  initial begin
    $display("Hello, %s!", name);
    $finish;
  end
endmodule
