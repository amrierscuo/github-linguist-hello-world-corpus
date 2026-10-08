from pathlib import Path
import json, sqlite3, importlib.metadata
import lkml
with Path('hello.lookml').open(encoding='utf-8') as stream: ast=lkml.load(stream)
view=ast['views'][0]
assert view['name']=='hello'
assert view['dimensions'][0]['sql']=='${TABLE}.greeting'
query=view['derived_table']['sql'].strip()
with sqlite3.connect(':memory:') as db:
 assert db.execute(query).fetchone()==('Hello, World!',)
print(json.dumps(dict(parser='lkml',version=importlib.metadata.version('lkml'),greeting='Hello, World!',scope='LookML parsed; embedded SQL executed by SQLite; Looker runtime pending'),ensure_ascii=False))
