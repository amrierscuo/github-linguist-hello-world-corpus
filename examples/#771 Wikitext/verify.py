from pathlib import Path
import mwparserfromhell
code=mwparserfromhell.parse(Path('hello.mediawiki').read_text())
assert len(code.filter_headings())==1 and str(code.filter_headings()[0].title).strip()=='Greeting'
assert 'Hello, World!' in code.strip_code()
print(code.strip_code().strip());print('PASS: existing MediaWiki source parser and plain-text/body model')
