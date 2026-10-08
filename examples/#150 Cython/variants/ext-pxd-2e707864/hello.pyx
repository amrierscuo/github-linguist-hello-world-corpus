# cython: language_level=3
cdef const char* greeting_text():
    return "Hello, World!"
def emit():
    print(greeting_text().decode("ascii"))
