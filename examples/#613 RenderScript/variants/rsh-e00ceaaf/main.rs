#pragma version(1)
#pragma rs java_package_name(org.corpus.greeting)
#include "rs_debug.rsh"
#include "hello.rsh"
void hello() { rsDebug(corpus_greeting, 0); }
