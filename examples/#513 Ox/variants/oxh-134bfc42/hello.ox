#include <oxstd.h>
#include "hello.oxh"
Greeting() { return "Hello, World!"; }
main() { print(Greeting(), "\n"); }
