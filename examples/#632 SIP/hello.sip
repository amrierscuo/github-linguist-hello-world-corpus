%Module(name=corpus_greeting, language="C")

%ModuleCode
const char *corpus_greeting(void) { return "Hello, World!"; }
%End

const char *corpus_greeting();
