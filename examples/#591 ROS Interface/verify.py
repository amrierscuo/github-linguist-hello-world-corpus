from pathlib import Path
from rosidl_adapter.parser import parse_message_string
value = parse_message_string("corpus", "Greeting", Path("Greeting.msg").read_text(encoding="utf-8"))
assert len(value.constants) == 1
assert value.constants[0].name == "GREETING"
assert value.constants[0].value == "Hello, World!"
assert len(value.fields) == 1 and value.fields[0].name == "message"
print(value.constants[0].value)
