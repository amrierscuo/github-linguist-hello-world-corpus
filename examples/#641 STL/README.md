# #641 STL

Caricare una mesh STL originale che costruisce il saluto con pixel estrusi.

## Verifica reale

Trimesh 4.9.0; Matplotlib 3.10.6; CPython 3.13.9

```text
pip install trimesh==4.9.0 matplotlib==3.10.6; python verify_render.py; aprire verification/top-view.png.
```

Risultato atteso: STL accettato; triangoli dei pixel estrusi mostrano Hello, World! dall’alto.

**Sintassi e semantica verificate.** Mesh originale caricata da Trimesh: 1668 triangoli, 278 triangoli sulla superficie superiore. La vista dall’alto è renderizzata dai soli triangoli STL, senza sovrapporre testo. Ispezione visiva: Hello, World! leggibile.

[Log della prova](verification/render.json). La precedente prova sintattica resta in [result.json](verification/result.json).

![Rendering del campione](verification/top-view.png)

## Fonti primarie

- [https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp](https://github.com/assimp/assimp/blob/master/code/AssetLib/STL/STLLoader.cpp)
- [https://trimesh.org/formats.html](https://trimesh.org/formats.html)
- [https://trimesh.org/trimesh.html](https://trimesh.org/trimesh.html)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.stl` | [hello.stl](hello.stl) sintassi e semantica verificate |
