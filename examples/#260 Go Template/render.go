package main

import (
    "bytes"
    "fmt"
    "html/template"
    "os"
)

func main() {
    compiled, err := template.ParseFiles("hello.gotmpl")
    if err != nil { panic(err) }
    render := func(recipient string) string {
        var buffer bytes.Buffer
        if err := compiled.Execute(&buffer, struct { Recipient string }{recipient}); err != nil { panic(err) }
        return buffer.String()
    }
    greeting := render("World")
    if greeting != "Hello, World!\n" { panic(greeting) }
    if render("<world>") != "Hello, &lt;world&gt;!\n" { panic("escaping mismatch") }
    fmt.Fprint(os.Stdout, greeting)
}
