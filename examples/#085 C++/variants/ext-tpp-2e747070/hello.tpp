#include <string>
template <typename Char>
std::basic_string<Char> corpus_greeting() {
 const char *text = "Hello, World!";
 return std::basic_string<Char>(text, text + 13);
}
