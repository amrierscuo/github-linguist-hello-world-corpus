import json
from pathlib import Path
data = json.loads(Path("hello.json").read_text(encoding="utf-8"))
assert data == {"greeting": "Hello, World!"}
print(data["greeting"])
