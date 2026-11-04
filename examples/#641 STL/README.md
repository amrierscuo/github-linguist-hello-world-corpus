# #641 STL

Upload an original mesh STL that builds greeting with extruded pixels.

## Real Verification

Trimesh 4.9.0; Matplotlib 3.10.6; CPython 3.13.9

```text
pip install trimesh==4.9.0 matplotlib==3.10.6; python verify_render.py; aprire verification/top-view.png.
```

Expected result: STL accepted; triangles of extruded pixels show Hello, World! from above.

**Sintassi e semantica verificate.** Original Mesh loaded by Trimesh: 1668 triangles, 278 triangles on the upper surface. The view from above is rendered by the only STL triangles, without overlapping text. Visual inspection: Hello, World! readable.

[Log della prova](verification/render.json). The previous syntactic test remains in [result.json](verification/result.json).

![Rendering del campione](verification/top-view.png)

## Primary sources

- [https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp](https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp)
- [https://trimesh.org/formats.html](https://trimesh.org/formats.html)
- [https://trimesh.org/trimesh.html](https://trimesh.org/trimesh.html)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.stl` | [hello.stl](hello.stl) syntax and behavior verified |
