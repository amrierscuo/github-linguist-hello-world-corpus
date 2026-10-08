from pathlib import Path
from docutils.core import publish_parts,publish_doctree
from docutils import nodes
source=Path('hello.rst').read_text()
tree=publish_doctree(source,settings_overrides={'halt_level':2,'report_level':2})
paragraphs=[p.astext() for p in tree.findall(nodes.paragraph)]
assert paragraphs==['Hello, World!']
parts=publish_parts(source,writer_name='html5',settings_overrides={'halt_level':2,'report_level':2})
assert 'Hello, <strong>World</strong>!' in parts['fragment']
print(paragraphs[0])
