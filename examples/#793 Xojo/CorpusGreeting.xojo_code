#tag Module
Protected Module CorpusGreeting
  #tag Method, Flags = &h0
    Function Greeting() As String
      Var audience As String = "World"
      Return "Hello, " + audience + "!"
    End Function
  #tag EndMethod
End Module
#tag EndModule
