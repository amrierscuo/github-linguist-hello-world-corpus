#include <iostream>
#include <string>
#include <objc/Object.h>
@interface Greeting : Object
+ (void)say;
@end
@implementation Greeting
+ (void)say { std::cout << std::string("Hello, World!") << std::endl; }
@end
int main() { [Greeting say]; return 0; }
