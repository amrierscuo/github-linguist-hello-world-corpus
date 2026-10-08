from pathlib import Path
from lark import Lark
parser = Lark.open('hello.lark', parser='lalr')
tree = parser.parse(Path('hello.txt').read_text(encoding='utf8'))
assert [str(x) for x in tree.children] == ['Hello', 'World']
print(tree.pretty(), end='')
