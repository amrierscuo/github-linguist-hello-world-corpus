tasks.register("hello") {
    doLast {
        val name = "World"
        println("Hello, $name!")
    }
}
