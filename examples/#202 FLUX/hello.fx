GetGreeting() => (char* message);
PrintGreeting(char* message) => ();

source GetGreeting => PrintGreeting;
