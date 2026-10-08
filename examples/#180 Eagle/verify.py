from pathlib import Path
import sys
from lxml import etree
source = Path(__file__).with_name('hello.sch')
with open(sys.argv[1], 'rb') as stream:
    dtd = etree.DTD(stream)
tree = etree.parse(str(source), etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True))
dtd.assertValid(tree)
assert tree.findtext('drawing/schematic/sheets/sheet/plain/text') == 'Hello, World!'
assert tree.find('drawing/schematic/sheets/sheet/plain/text').get('layer') == '97'
print('EAGLE vendor DTD 7.7.0 validation PASS; original text object on Info layer 97.')
print('CAD rendering still pending.')
