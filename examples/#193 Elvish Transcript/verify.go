package main

import (
    "bytes"
    "fmt"
    "os"
    "os/exec"
    "src.elv.sh/pkg/transcript"
)

func main() {
    input, err := os.Open("hello.elvts")
    if err != nil { panic(err) }
    defer input.Close()
    tree, err := transcript.Parse("hello.elvts", input)
    if err != nil { panic(err) }
    if len(tree.Interactions) != 1 || len(tree.Children) != 0 { panic("expected one interaction") }
    interaction := tree.Interactions[0]
    if interaction.Output != "Hello, World!\n" { panic("unexpected recorded output") }
    binary := "elvish"
    if len(os.Args) > 1 { binary = os.Args[1] }
    command := exec.Command(binary, "-c", interaction.Code)
    output, err := command.Output()
    if err != nil { panic(err) }
    if !bytes.Equal(output, []byte(interaction.Output)) { panic("runtime output differs from transcript") }
    fmt.Print(string(output))
}
