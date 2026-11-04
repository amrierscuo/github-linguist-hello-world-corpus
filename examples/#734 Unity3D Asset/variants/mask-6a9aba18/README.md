# Unity3D Asset: variant .mask

Questo esempio è un asset Unity YAML nativo di tipo `AvatarMask` (classID `319`), adattato da un file reale del repository primario `giacomelli/unity-avatar-mask-and-animation-layers`, pubblicato da Diego Giacomelli, autore del tutorial originale. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `UpperBody` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `1f267607f39ef842a991972e386b1ca2243408b1`, con SHA256 dell’originale e confronto con SHA256 dell’originale recuperato indipendentemente. Nessun asset di un tipo diverso viene rinominato come .mask.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `2019.1.3f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Provisional verification procedure: In compatible separate Unity project, import hello.mask; check in the inspector the type AvatarMask and name == "Hello, World!".

Expected result: a `AvatarMask` object called `Hello, World!`. Dependencies to solve in the Unity environment: The original AvatarMask file contains no external rig/mesh references (m_Elements: []); the actual masking should be tried with an Avatar in its Unity project.

License: `MIT`. `LICENSE_UPSTREAM.md` retains without modification the copyright and license text published by the repository. The notice MIT remains included with this adapted copy.

Primary sources:

- [Asset originale, commit immutabile](https://github.com/giacomelli/unity-avatar-mask-and-animation-layers/blob/1f267607f39ef842a991972e386b1ca2243408b1/avatar-mask-complete/Assets/_Tutorial/Animations/UpperBody.mask)
- [Licenza originale](https://github.com/giacomelli/unity-avatar-mask-and-animation-layers/blob/1f267607f39ef842a991972e386b1ca2243408b1/LICENSE)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo AvatarMask](https://docs.unity3d.com/ScriptReference/AvatarMask.html)

The author’s primary source explains the creation of this AvatarMask via Assets/Create/Avatar Mask. This fixture retains the author’s MIT license; it does not include other files, models or tutorial animations.

- [Tutorial originale dell’autore](https://diegogiacomelli.com.br/unity-avatar-mask-and-animation-layers/)
