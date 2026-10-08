from pathlib import Path
import jinja2,sys
env = jinja2.Environment(undefined=jinja2.StrictUndefined, keep_trailing_newline=True)
template = env.from_string(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert template.render(name='World') == 'Hello, World!\n'
assert template.render(name='Reader') == 'Hello, Reader!\n'
try: template.render()
except jinja2.UndefinedError: pass
else: raise AssertionError('Missing name unexpectedly accepted')
print(template.render(name='World'), end='')
print('PASS: native Jinja compile/render and parameter controls')
