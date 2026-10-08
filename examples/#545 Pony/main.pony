actor Main
  new create(env: Env) =>
    let audience = "World"
    env.out.print("Hello, " + audience + "!")
