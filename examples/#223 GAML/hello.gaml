model corpus_greeting

global {
    init {
        write "Hello, " + "World!";
    }
}

experiment greeting type: gui {
}
