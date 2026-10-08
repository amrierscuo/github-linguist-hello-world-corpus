#include <cstdio>
#include <cstdlib>
#include "mImpl.h"

void init(int, char**) {}

int GetGreeting(GetGreeting_out* output) {
    static char message[] = "Hello, World!";
    output->message = message;
    return 0;
}

int PrintGreeting(PrintGreeting_in* input) {
    int status = std::puts(input->message);
    std::fflush(stdout);
    std::exit(status < 0 ? 1 : 0);
}
