# Unity3D Asset — variante .mat

Questo esempio è un asset Unity YAML nativo di tipo `Material` (classID `21`), adattato da un file reale del repository primario `Unity-Technologies/ml-agents`, pubblicato da Unity Technologies. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `UIDefault` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9`, con SHA256 dell’originale e confronto del blob Git con l’albero upstream. Nessun asset di un tipo diverso viene rinominato come .mat.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `6000.0.77f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Procedura di verifica prevista: In progetto Unity separato compatibile, importare hello.mat; controllare nell’Inspector il tipo Material e name == "Hello, World!".

Risultato atteso: un oggetto `Material` chiamato `Hello, World!`. Dipendenze da risolvere nell’ambiente Unity: Lo shader è il riferimento built-in Unity fileID 10782, GUID 0000000000000000f000000000000000; risoluzione da verificare nella libreria dell’Editor originale.

Licenza: `Apache-2.0`. `LICENSE_UPSTREAM.md` conserva senza modifiche il copyright e il testo di licenza pubblicato dal repository. Il testo completo Apache-2.0 è incluso in LICENSE-APACHE-2.0.txt. Questa modifica al nome è dichiarata qui e nella provenienza.

Fonti primarie:

- [Asset originale, commit immutabile](https://github.com/Unity-Technologies/ml-agents/blob/2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9/Project/Assets/ML-Agents/Examples/SharedAssets/Materials/UIDefault.mat)
- [Licenza originale](https://github.com/Unity-Technologies/ml-agents/blob/2f97e1cbb408fe40169b720aa82a46f3f8a0a8e9/LICENSE.md)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo Material](https://docs.unity3d.com/ScriptReference/Material.html)
