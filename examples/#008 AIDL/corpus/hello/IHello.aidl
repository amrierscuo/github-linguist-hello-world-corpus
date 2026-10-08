package corpus.hello;

// Contratto Binder: il saluto è una costante condivisa da client e server.
interface IHello {
    const String GREETING = "Hello, World!";
    String getGreeting();
}
