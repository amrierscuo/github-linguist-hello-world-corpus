import json
from pathlib import Path
from pyld import jsonld
value = json.loads(Path("hello.jsonld").read_text(encoding="utf-8"))
expanded = jsonld.expand(value)
assert expanded == [{"@id": "https://example.invalid/hello", "https://example.invalid/vocab/greeting": [{"@value": "Hello, World!"}]}]
print(expanded[0]["https://example.invalid/vocab/greeting"][0]["@value"])
