from pathlib import Path
from gemtext import Gemtext, Heading, Paragraph
document = Gemtext(Path("hello.gmi").read_text(encoding="utf-8"))
headings = [str(item) for item in document.content if isinstance(item, Heading)]
paragraphs = [str(item) for item in document.content if isinstance(item, Paragraph) and str(item)]
assert headings == ["Corpus greeting"]
assert paragraphs == ["Hello, World!"]
print("PASS: Gemini paragraph = Hello, World!")
