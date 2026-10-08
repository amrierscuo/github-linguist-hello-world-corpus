from pathlib import Path
import sys
import bbcode

source = Path(sys.argv[1] if len(sys.argv) > 1 else 'hello.bbcode').read_text(encoding='utf-8').strip()
parser = bbcode.Parser()
rendered = parser.format(source)
assert rendered == '<strong>Hello, World!</strong>', rendered
assert parser.format('[i]Hello, World![/i]') == '<em>Hello, World!</em>'
print(rendered)
print('PASS: genuine bbcode renderer, bold greeting and italic control')
