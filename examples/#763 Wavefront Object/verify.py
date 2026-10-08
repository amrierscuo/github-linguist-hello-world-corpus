import trimesh,numpy as np
scene=trimesh.load_scene('hello.obj')
print('GEOMETRY:',list(scene.geometry))
assert len(scene.geometry)==1
mesh=next(iter(scene.geometry.values()))
assert mesh.vertices.shape==(3,3) and mesh.faces.shape==(1,3)
assert np.allclose(mesh.bounds,[[0,0,0],[1,1,0]])
assert mesh.visual.material.name=='Hello, World!'
print(mesh.visual.material.name);print('PASS: existing OBJ loader resolves original labelled triangle and MTL')
