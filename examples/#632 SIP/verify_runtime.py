"""Check the greeting returned by the compiled SIP extension."""
import corpus_greeting

greeting = corpus_greeting.corpus_greeting()
if isinstance(greeting, bytes):
    greeting = greeting.decode("utf-8")
assert greeting == "Hello, World!", repr(greeting)
print(greeting)
