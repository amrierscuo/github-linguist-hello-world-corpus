#include <iostream>
const char *scan(const char *YYCURSOR) {
 const char *YYMARKER;
 /*!re2c
 re2c:define:YYCTYPE = char;
 "World" { return "Hello, World!"; }
 * { return "unexpected input"; }
 */
}
int main() { std::cout << scan("World") << "\n"; }
