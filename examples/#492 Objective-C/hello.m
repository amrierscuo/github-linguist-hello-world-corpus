#include <stdio.h>
#include <objc/Object.h>
@interface Greeting : Object
+ (void)say;
@end
@implementation Greeting
+ (void)say { puts("Hello, World!"); }
@end
int main(void) { [Greeting say]; return 0; }
