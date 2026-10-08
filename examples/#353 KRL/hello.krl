ruleset io.corpus.greeting {
  rule greet {
    select when corpus hello
    send_directive("greeting", {"message": "Hello, World!"})
  }
}
