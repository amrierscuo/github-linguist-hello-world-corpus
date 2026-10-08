from pathlib import Path
import pystache,sys
template=Path(sys.argv[1]).read_text(encoding='utf-8')
renderer=pystache.Renderer(missing_tags='strict')
assert renderer.render(template,{'name':'World'})=='Hello, World!\n'
assert renderer.render(template,{'name':'<Reader>'})=='Hello, &lt;Reader&gt;!\n'
print(renderer.render(template,{'name':'World'}),end='')
print('PASS: existing Mustache renderer, context value and escaping control')
