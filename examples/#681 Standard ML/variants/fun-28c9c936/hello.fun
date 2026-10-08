functor GreetingFn () = struct
  fun message () = "Hello, World!"
end;
structure Greeting = GreetingFn ();
val _ = print (Greeting.message () ^ "\n");
