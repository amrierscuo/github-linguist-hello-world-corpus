from pathlib import Path
from genshi.template import MarkupTemplate
template = MarkupTemplate(Path("hello.kid").read_text(encoding="utf-8"))
rendered = template.generate(audience="World").render("xhtml").strip()
assert rendered == "<p>Hello, World!</p>", rendered
print(rendered)
