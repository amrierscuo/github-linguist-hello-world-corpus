module consumer;
import greeting;
extern(C) int puts(const char* text);
extern(C) int main() { return puts(greeting_text()) < 0 ? 1 : 0; }
