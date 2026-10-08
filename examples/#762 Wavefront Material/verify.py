from pathlib import Path
import numpy as np
from trimesh.exchange.obj import parse_mtl
model=parse_mtl(Path('hello.mtl').read_text())
print(repr(model))
assert 'Hello, World!' in model
assert np.allclose(model['Hello, World!']['diffuse'],[.8,.4,.1])
print('Hello, World!');print('PASS: existing Wavefront MTL decoder validates name and diffuse color')
