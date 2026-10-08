from pathlib import Path
from markdown_it import MarkdownIt
source = Path("hello.mdwn").read_text(encoding="utf-8")
html = MarkdownIt("commonmark").render(source)
assert html == "<h1>Hello, World!</h1>\n"
print("Hello, World!")
