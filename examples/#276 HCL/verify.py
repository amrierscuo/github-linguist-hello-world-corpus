from pathlib import Path
import hcl2,sys
with Path(sys.argv[1]).open(encoding='utf-8') as stream: data = hcl2.load(stream)
assert data == {'message': 'Hello, World!'}, data
print(data['message'])
print('PASS: existing HCL2 parser and literal attribute value')
