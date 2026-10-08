from pathlib import Path
import tree_sitter_python
from tree_sitter import Language,Parser,Query,QueryCursor
language=Language(tree_sitter_python.language())
parser=Parser(language)
tree=parser.parse(Path("hello.py").read_bytes())
assert not tree.root_node.has_error
query=Query(language,Path("hello.scm").read_text())
captures=QueryCursor(query).captures(tree.root_node)
assert [n.text.decode() for n in captures["function"]]==["print"]
assert [n.text.decode() for n in captures["greeting"]]==["Hello, World!"]
print(captures["greeting"][0].text.decode())
