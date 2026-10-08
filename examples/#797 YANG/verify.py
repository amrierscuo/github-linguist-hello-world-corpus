from pathlib import Path
from pyang import context, repository
ctx = context.Context(repository.FileRepository("."))
module = ctx.add_module("corpus-greeting.yang", Path("corpus-greeting.yang").read_text(encoding="utf8"))
ctx.validate()
assert module and not ctx.errors, ctx.errors
leaf = module.search_one("leaf", "greeting")
assert leaf.search_one("type").arg == "string"
actual = leaf.search_one("default").arg
assert actual == "Hello, World!"
print(actual)
