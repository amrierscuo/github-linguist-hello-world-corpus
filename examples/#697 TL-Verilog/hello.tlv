\TLV_version 1a: tl-x.org
\SV
module hello;
wire [103:0] message;
initial begin
  #1; $display("%s", message); $finish;
end
\TLV
   |greeting
      @0
         $message[103:0] = 104'h48656c6c6f2c20576f726c6421;
         *message = $message;
\SV
endmodule
