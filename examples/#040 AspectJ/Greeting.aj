public aspect Greeting {
    before(): execution(void HelloWorld.greet()) {
        System.out.println("Hello, World!");
    }
}
