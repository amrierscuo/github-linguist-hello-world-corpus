from pathlib import Path
import sys
from creoleparser import Parser, create_dialect
from creoleparser.dialects import creole10_base

renderer = Parser(create_dialect(creole10_base))
result = renderer.render(Path(sys.argv[1]).read_text(encoding="utf-8"))
if isinstance(result, bytes):
    result = result.decode("utf-8")
assert "<h1>Greeting</h1>" in result, result
assert "<strong>Hello, World!</strong>" in result, result
assert "<em>A small Creole document.</em>" in result, result
print(result, end="" if result.endswith("\n") else "\n")
print("PASS: existing Creole 1.0 renderer; heading, strong and emphasis")
