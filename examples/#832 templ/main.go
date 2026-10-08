package main
import ("context"; "os"; "bytes"; "strings")
func main() { var b bytes.Buffer; if err:=Hello("World").Render(context.Background(),&b); err!=nil { panic(err) }; if !strings.Contains(b.String(),"<h1>Hello, World!</h1>") { panic(b.String()) }; os.Stdout.Write(b.Bytes()) }
