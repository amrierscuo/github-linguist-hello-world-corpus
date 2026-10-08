rule CorpusGreeting {
    strings:
        $greeting = "Hello, World!"
    condition:
        $greeting
}
