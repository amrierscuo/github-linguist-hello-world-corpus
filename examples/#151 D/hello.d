module hello;

extern(C) int puts(const char* message);

const(char)* greeting() @nogc nothrow
{
    return "Hello, World!".ptr;
}

extern(C) int main()
{
    return puts(greeting()) < 0 ? 1 : 0;
}
