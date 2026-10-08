from pathlib import Path
from openstep_parser import OpenStepDecoder
value = OpenStepDecoder.ParseFromString(Path("hello.plist").read_text(encoding="utf-8"))
assert value == {"greeting": "Hello, World!"}
print(value["greeting"])
