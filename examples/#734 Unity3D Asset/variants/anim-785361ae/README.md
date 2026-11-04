# Unity3D Asset: variant .anim

Questo esempio è un asset Unity YAML nativo di tipo `AnimationClip` (classID `74`), adattato da un file reale del repository primario `Unity-Technologies/2d-techdemos`, pubblicato da Unity Technologies. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `explosion` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `6593d544df2ea598e51f5cf1d7165d5ed42ceba7`, con SHA256 dell’originale e confronto del blob Git con l’albero upstream. Nessun asset di un tipo diverso viene rinominato come .anim.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `6000.3.3f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Provisional verification procedure: In compatible separate Unity project, import hello.anim; check in the inspector the type AnimationClip and name == "Hello, World!".

Expected result: a `AnimationClip` object called `Hello, World!`. Dependencies to solve in the environment Unity: Sprite maker and original atlas with GUID 195d2ebbbf668124ab3fa9932a849bcb: the original graphics are not included in this example.

License: `MIT`. `LICENSE_UPSTREAM.md` retains without modification the copyright and license text published by the repository. The notice MIT remains included with this adapted copy.

Primary sources:

- [Asset originale, commit immutabile](https://github.com/Unity-Technologies/2d-techdemos/blob/6593d544df2ea598e51f5cf1d7165d5ed42ceba7/Assets/Tilemap/Destructible/Explosion/explosion.anim)
- [Licenza originale](https://github.com/Unity-Technologies/2d-techdemos/blob/6593d544df2ea598e51f5cf1d7165d5ed42ceba7/LICENSE.md)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo AnimationClip](https://docs.unity3d.com/ScriptReference/AnimationClip.html)
