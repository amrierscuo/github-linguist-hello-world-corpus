.assembly extern mscorlib {}
.assembly Hello {}
.module Hello.exe

.class public auto ansi Hello extends [mscorlib]System.Object {
  .method public static void Main() cil managed {
    .entrypoint
    .maxstack 1
    ldstr "Hello, World!"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
  }
}
