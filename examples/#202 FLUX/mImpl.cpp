#include <atomic>
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
    static std::atomic_flag printed = ATOMIC_FLAG_INIT;
    if (printed.test_and_set(std::memory_order_relaxed)) return 0;
    int status = std::puts(input->message);
    std::fflush(stdout);
    std::exit(status < 0 ? 1 : 0);
}
