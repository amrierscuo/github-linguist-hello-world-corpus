from pathlib import Path
import sys
import xml.etree.ElementTree as ET
root = ET.parse(Path(sys.argv[1])).getroot()
texts = [''.join(node.itertext()) for node in root.iter('{http://www.w3.org/2000/svg}text')]
assert 'Hello, World!' in texts, texts
print('Hello, World!')
print('PASS: genuine Graphviz SVG contains the node label')
