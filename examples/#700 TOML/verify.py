from pathlib import Path
import tomllib
with Path('hello.toml').open('rb') as f:data=tomllib.load(f)
assert data=={'greeting':{'message':'Hello, World!','language':'en'}}
print(data['greeting']['message']);print('PASS: native TOML parser and exact configuration model')
