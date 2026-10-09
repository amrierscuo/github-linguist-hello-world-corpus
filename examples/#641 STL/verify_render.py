"""Render the actual STL triangles in top view; requires trimesh and matplotlib."""
from pathlib import Path
import hashlib
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np
import trimesh

source = Path(__file__).with_name("hello.stl")
mesh = trimesh.load_mesh(source, file_type="stl")
assert isinstance(mesh, trimesh.Trimesh) and len(mesh.faces) > 0
triangles = mesh.triangles
top = triangles[np.all(np.isclose(triangles[:, :, 2], mesh.bounds[1, 2]), axis=1)]
assert len(top) > 0
fig, ax = plt.subplots(figsize=(15, 2.4), dpi=120)
fig.patch.set_facecolor("#101923")
ax.set_facecolor("#101923")
ax.add_collection(PolyCollection(top[:, :, :2], facecolors="#65e6cb", edgecolors="none"))
ax.set_xlim(mesh.bounds[0, 0] - 2, mesh.bounds[1, 0] + 2)
ax.set_ylim(mesh.bounds[0, 1] - 2, mesh.bounds[1, 1] + 2)
ax.set_aspect("equal")
ax.axis("off")
destination = source.parent / "verification" / "top-view.png"
destination.parent.mkdir(exist_ok=True)
fig.savefig(destination, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print(json.dumps({"source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                  "trimesh": trimesh.__version__, "matplotlib": matplotlib.__version__,
                  "vertices": len(mesh.vertices), "faces": len(mesh.faces),
                  "bounds": mesh.bounds.tolist(), "top_triangles": len(top),
                  "image": destination.name,
                  "image_sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}))
