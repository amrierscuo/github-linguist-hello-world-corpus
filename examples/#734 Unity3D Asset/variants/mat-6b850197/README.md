# Unity3D Asset: variant .mat

Questo esempio è un asset Unity YAML nativo di tipo `Material` (classID `21`), adattato da un file reale del repository primario `Unity-Technologies/ml-agents`, pubblicato da Unity Technologies. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `UIDefault` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9`, con SHA256 dell’originale e confronto del blob Git con l’albero upstream. Nessun asset di un tipo diverso viene rinominato come .mat.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `6000.0.77f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Provisional verification procedure: In compatible separate Unity project, import hello.mat; check in the Inspector the Material type and name == "Hello, World!".

Expected result: a `Material` object called `Hello, World!`. Dependencies to solve in the environment Unity: Shadingr is the built-in Unity fileID 10782, GUID 0000000000000000f000000000000000; resolution to check in the library of the original Editor.

License: `Apache-2.0`. `LICENSE_UPSTREAM.md` without modification retains the copyright and license text published by the repository. The full text Apache-2.0 is included in LICENSE-APACHE-2.0.txt.

Primary sources:

- [Asset originale, commit immutabile](https://github.com/Unity-Technologies/ml-agents/blob/2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9/Project/Assets/ML-Agents/Examples/SharedAssets/Materials/UIDefault.mat)
- [Licenza originale](https://github.com/Unity-Technologies/ml-agents/blob/2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9/LICENSE.md)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo Material](https://docs.unity3d.com/ScriptReference/Material.html)
