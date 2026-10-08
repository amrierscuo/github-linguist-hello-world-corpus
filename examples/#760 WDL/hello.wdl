version 1.0
task hello {
    command <<<
        printf "Hello, World!\n"
    >>>
    output { String greeting = read_string(stdout()) }
}
workflow greeting {
    call hello
    output { String message = hello.greeting }
}
