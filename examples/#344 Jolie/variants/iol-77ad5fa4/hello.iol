type Greeting: string

interface GreetingPort {
  OneWay: greet(Greeting)
}
