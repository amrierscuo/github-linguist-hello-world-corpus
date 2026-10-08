module hello

one sig Greeting {
  text: one String
}

fact ExactText {
  Greeting.text = "Hello, World!"
}

pred showGreeting {
  one Greeting
}

assert GreetingIsHelloWorld {
  all g: Greeting | g.text = "Hello, World!"
}

run showGreeting for 3 expect 1
check GreetingIsHelloWorld for 3 expect 0
