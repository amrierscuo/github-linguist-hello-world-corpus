rendered = EEx.eval_file("hello.html.eex", audience: "World")
if rendered != "<p>Hello, World!</p>\n", do: raise("Unexpected rendering")
IO.write(rendered)
