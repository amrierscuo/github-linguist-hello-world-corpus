#import "hello.h"
NSString *CorpusGreeting(void) { return @"Hello, World!"; }
int main(void) { @autoreleasepool { puts([CorpusGreeting() UTF8String]); } return 0; }
