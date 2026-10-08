schema Greeting:
    name: str = "World"
    message: str = "Hello, ${name}!"

greeting = Greeting {}
