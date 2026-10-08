import json5
from pathlib import Path
value = json5.loads(Path("hello.json5").read_text(encoding="utf-8"))
assert value == {"greeting": "Hello, World!"}
print(value["greeting"])
