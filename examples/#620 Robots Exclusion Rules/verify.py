from pathlib import Path
from urllib.robotparser import RobotFileParser
p=RobotFileParser();p.parse(Path('robots.txt').read_text().splitlines())
assert p.can_fetch('CorpusBot','https://example.invalid/hello.txt')
assert not p.can_fetch('CorpusBot','https://example.invalid/private/file')
assert Path('hello.txt').read_text()=='Hello, World!\n'
print('Hello, World!')
print('PASS: native robots parser permits local greeting path and rejects private control; no network access')
