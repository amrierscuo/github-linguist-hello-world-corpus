module Hello

open FStar.All

let main () : ML unit =
  FStar.IO.print_string "Hello, World!\n"
