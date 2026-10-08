%module hello
%inline %{
const char *greeting(void) { return "Hello, World!"; }
%}
