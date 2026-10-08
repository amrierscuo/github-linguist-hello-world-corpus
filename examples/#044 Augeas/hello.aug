module Hello =
  let lns = [ label "greeting" . store /Hello, World!/ . del "\n" "\n" ]
  test lns get "Hello, World!\n" = { "greeting" = "Hello, World!" }
  test lns put "Hello, World!\n" after set "/greeting" "Hello, World!" = "Hello, World!\n"
