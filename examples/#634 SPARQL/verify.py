from pathlib import Path
from rdflib import Graph
rows = list(Graph().query(Path("hello.rq").read_text(encoding="utf8")))
assert len(rows) == 1
actual = str(rows[0].greeting)
assert actual == "Hello, World!"
print(actual)
