from pathlib import Path
import html5lib,sys
parser = html5lib.HTMLParser(strict=True)
document = parser.parse(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert parser.errors == [], parser.errors
ns = {'html': 'http://www.w3.org/1999/xhtml'}
assert document.attrib['lang'] == 'en'
assert document.find('html:head/html:title', ns).text == 'Greeting'
heading = document.find('html:body/html:main/html:h1', ns)
assert heading is not None and ''.join(heading.itertext()) == 'Hello, World!'
print(heading.text)
print('PASS: existing HTML5 parser, strict document and visible heading DOM')
