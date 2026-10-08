from pathlib import Path
from kivy.lang.parser import Parser
p=Parser(content=Path("hello.kv").read_text(),filename="hello.kv")
assert p.root.name=="Label"
assert "text" in p.root.properties and "font_size" in p.root.properties
print("Kivy Parser PASS")
