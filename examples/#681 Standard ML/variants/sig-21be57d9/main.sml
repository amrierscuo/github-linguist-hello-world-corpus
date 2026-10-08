use "hello.sig";
structure Greeting : GREETING = struct val message = "Hello, World!" end;
val _ = print (Greeting.message ^ "\n");
