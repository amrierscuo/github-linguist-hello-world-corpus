from pathlib import Path
import ctypes as c
import sys
lib = c.CDLL(sys.argv[1])
def api(name, result, args):
    f = getattr(lib, name); f.restype = result; f.argtypes = args; return f
ptr = c.c_void_p
context_new = api("xkb_context_new", ptr, [c.c_int])
table_new = api("xkb_compose_table_new_from_buffer", ptr, [ptr, c.c_char_p, c.c_size_t, c.c_char_p, c.c_int, c.c_int])
state_new = api("xkb_compose_state_new", ptr, [ptr, c.c_int])
feed = api("xkb_compose_state_feed", c.c_int, [ptr, c.c_uint])
status = api("xkb_compose_state_get_status", c.c_int, [ptr])
utf8 = api("xkb_compose_state_get_utf8", c.c_int, [ptr, c.c_void_p, c.c_size_t])
context = context_new(0)
data = Path("XCompose").read_bytes()
table = table_new(context, data, len(data), b"C.UTF-8", 1, 0)
assert table
state = state_new(table, 0)
try:
    for key in (0xff20, ord("h"), ord("w")): assert feed(state, key) == 1
    assert status(state) == 2
    buffer = c.create_string_buffer(100)
    assert utf8(state, buffer, 100) == 13
    actual = buffer.value.decode("utf8")
    assert actual == "Hello, World!"
    print(actual)
finally:
    api("xkb_compose_state_unref", None, [ptr])(state)
    api("xkb_compose_table_unref", None, [ptr])(table)
    api("xkb_context_unref", None, [ptr])(context)
