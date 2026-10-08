from pathlib import Path
import re
pattern=re.compile(Path('hello.regexp').read_text().rstrip('\n'))
assert pattern.fullmatch('Hello, World!').group('name')=='World'
assert pattern.fullmatch('Hello, Reader!') is None
assert pattern.fullmatch('Hello, World!?') is None
print('Hello, '+pattern.fullmatch('Hello, World!').group('name')+'!')
print('PASS: authentic Python re compile/fullmatch and rejection controls')
