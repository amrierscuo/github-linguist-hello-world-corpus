int main() { object m = compile_file("hello.pmod")(); write("%s\n", m->greeting()); return 0; }
