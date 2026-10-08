package main
import("fmt";"os";"go.starlark.net/starlark")
func main(){
 observed:=[]string{}
 thread:=&starlark.Thread{Name:"corpus",Print:func(_ *starlark.Thread,msg string){observed=append(observed,msg);fmt.Println(msg)}}
 globals,err:=starlark.ExecFile(thread,os.Args[1],nil,nil);if err!=nil{panic(err)}
 if len(observed)!=1||observed[0]!="Hello, World!"{panic("unexpected print")}
 value,err:=starlark.Call(thread,globals["greet"],starlark.Tuple{starlark.String("Reader")},nil)
 if err!=nil||value!=starlark.String("Hello, Reader!"){panic("parameter control failed")}
 fmt.Println("PASS: authentic Google Starlark evaluator and parameter control")
}
