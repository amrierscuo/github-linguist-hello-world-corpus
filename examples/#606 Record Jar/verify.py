from pathlib import Path
from language_data.registry_parser import parse_file
with Path('language-subtag-registry.txt').open(encoding='utf-8') as f:records=list(parse_file(f))
assert len(records)==1 and records[0]['Subtag']=='qaa'
assert records[0]['Description']==['Hello, World!']
assert records[0]['Type']=='language'
print(records[0]['Description'][0])
print('PASS: existing language-data native Record Jar registry parser')
