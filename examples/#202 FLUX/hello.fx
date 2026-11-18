GetGreeting() => (greeting_chars message);
PrintGreeting(greeting_chars message) => ();

GreetingFlow(greeting_chars message) => ();

source GetGreeting => GreetingFlow;

GreetingFlow = PrintGreeting;
