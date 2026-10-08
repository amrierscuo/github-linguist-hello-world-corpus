#include "share/atspre_staload.hats"
staload "./hello.sats"
implement greeting () = "Hello, World!"
implement main0 () = println! (greeting ())
