from pathlib import Path
import configparser
p = configparser.ConfigParser(interpolation=None, strict=True)
p.read(Path(__file__).with_name('hello.ini'), encoding='utf-8')
assert p.sections() == ['greeting']
assert p['greeting']['message'] == 'Hello, World!'
print(p['greeting']['message'])
