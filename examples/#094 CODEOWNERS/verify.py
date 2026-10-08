from pathlib import Path
from codeowners import CodeOwners
import importlib.metadata
owners = CodeOwners(Path('CODEOWNERS').read_text(encoding='utf-8'))
matched = owners.of('hello.txt')
assert matched == [('EMAIL', 'hello@example.invalid')], matched
assert owners.of('other.txt') == []
print(f'codeowners {importlib.metadata.version("codeowners")}: local path match PASS: {matched}')
print('GitHub account eligibility and review assignment remain unverified; email is illustrative.')
