from pathlib import Path
from html.parser import HTMLParser
import textile
actual = textile.textile(Path("hello.textile").read_text(encoding="utf8"))
assert actual.strip() == "<p>Hello, <strong>World</strong>!</p>"
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []
    def handle_data(self, data): self.parts.append(data)
p = Text(); p.feed(actual)
text = "".join(p.parts).strip()
assert text == "Hello, World!"
print(text)
