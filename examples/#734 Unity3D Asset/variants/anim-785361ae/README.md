# Unity3D Asset — variante .anim

Questo esempio è un asset Unity YAML nativo di tipo `AnimationClip` (classID `74`), adattato da un file reale del repository primario `Unity-Technologies/2d-techdemos`, pubblicato da Unity Technologies. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `explosion` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `6593d544df2ea598e51f5cf1d7165d5ed42ceba7`, con SHA256 dell’originale e confronto del blob Git con l’albero upstream. Nessun asset di un tipo diverso viene rinominato come .anim.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `6000.3.3f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Procedura di verifica prevista: In progetto Unity separato compatibile, importare hello.anim; controllare nell’Inspector il tipo AnimationClip e name == "Hello, World!".

Risultato atteso: un oggetto `AnimationClip` chiamato `Hello, World!`. Dipendenze da risolvere nell’ambiente Unity: Sprite renderer e atlas originale con GUID 195d2ebbbf668124ab3fa9932a849bcb: la grafica originale non è inclusa in questo esempio.

Licenza: `MIT`. `LICENSE_UPSTREAM.md` conserva senza modifiche il copyright e il testo di licenza pubblicato dal repository. La notice MIT rimane inclusa con questa copia adattata. Questa modifica al nome è dichiarata qui e nella provenienza.

Fonti primarie:

- [Asset originale, commit immutabile](https://github.com/Unity-Technologies/2d-techdemos/blob/6593d544df2ea598e51f5cf1d7165d5ed42ceba7/Assets/Tilemap/Destructible/Explosion/explosion.anim)
- [Licenza originale](https://github.com/Unity-Technologies/2d-techdemos/blob/6593d544df2ea598e51f5cf1d7165d5ed42ceba7/LICENSE.md)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo AnimationClip](https://docs.unity3d.com/ScriptReference/AnimationClip.html)
