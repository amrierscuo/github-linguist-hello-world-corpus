from pathlib import Path
import sys
import collada
import numpy as np
from lxml import etree

if len(sys.argv) != 2:
    raise SystemExit('Usage: python verify.py /path/to/collada_schema_1_4_1.xsd')
schema_path = Path(sys.argv[1])
schema = etree.XMLSchema(etree.parse(str(schema_path)))
document = etree.parse('hello.dae')
schema.assertValid(document)
asset = collada.Collada('hello.dae')
assert not asset.errors, asset.errors
assert asset.assetInfo.title == 'Hello, World!'
assert asset.scene.id == 'GreetingScene'
assert len(asset.scene.nodes) == 1
node = asset.scene.nodes[0]
assert node.id == 'GreetingNode'
assert node.xmlnode.get('name') == 'HelloWorld'
assert np.array_equal(node.matrix, np.identity(4, dtype=np.float32))
print(f'Khronos COLLADA 1.4.1 XSD: valid; pycollada {collada.__version__}: greeting title, scene node and identity transform PASS.')
