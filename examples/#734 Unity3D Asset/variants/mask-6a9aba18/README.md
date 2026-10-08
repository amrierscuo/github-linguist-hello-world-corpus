# Unity3D Asset — variante .mask

Questo esempio è un asset Unity YAML nativo di tipo `AvatarMask` (classID `319`), adattato da un file reale del repository primario `giacomelli/unity-avatar-mask-and-animation-layers`, pubblicato da Diego Giacomelli, autore del tutorial originale. Il saluto è il valore della proprietà `m_Name`, consultabile nell’Inspector: non è una promessa di stampa a console o di testo disegnato dall’asset.

L’unica modifica ai byte dell’asset è `UpperBody` → `"Hello, World!"` nel campo `m_Name`. Curve, proprietà, riferimenti, identificatori e versioni di serializzazione originali sono conservati. La provenienza è ancorata al commit `1f267607f39ef842a991972e386b1ca2243408b1`, con SHA256 dell’originale e confronto con SHA256 dell’originale recuperato indipendentemente. Nessun asset di un tipo diverso viene rinominato come .mask.

Toolchain prevista: Unity Editor; versione dichiarata dal progetto upstream `2019.1.3f1`. L’Editor non è stato eseguito qui. Sintassi verificata: **false**. Semantica verificata: **false**. I controlli di provenienza in `verification/provenance.json` sono confronti di byte e hash, non verifiche del parser Unity.

Procedura di verifica prevista: In progetto Unity separato compatibile, importare hello.mask; controllare nell’Inspector il tipo AvatarMask e name == "Hello, World!".

Risultato atteso: un oggetto `AvatarMask` chiamato `Hello, World!`. Dipendenze da risolvere nell’ambiente Unity: Il file AvatarMask originale non contiene riferimenti a rig/mesh esterni (m_Elements: []); il mascheramento effettivo va provato con un Avatar nel proprio progetto Unity.

Licenza: `MIT`. `LICENSE_UPSTREAM.md` conserva senza modifiche il copyright e il testo di licenza pubblicato dal repository. La notice MIT rimane inclusa con questa copia adattata. Questa modifica al nome è dichiarata qui e nella provenienza.

Fonti primarie:

- [Asset originale, commit immutabile](https://github.com/giacomelli/unity-avatar-mask-and-animation-layers/blob/1f267607f39ef842a991972e386b1ca2243408b1/avatar-mask-complete/Assets/_Tutorial/Animations/UpperBody.mask)
- [Licenza originale](https://github.com/giacomelli/unity-avatar-mask-and-animation-layers/blob/1f267607f39ef842a991972e386b1ca2243408b1/LICENSE)
- [Formato testuale Unity](https://docs.unity3d.com/Manual/FormatDescription.html)
- [Tipo AvatarMask](https://docs.unity3d.com/ScriptReference/AvatarMask.html)

La fonte primaria dell’autore spiega la creazione di questo AvatarMask tramite Assets/Create/Avatar Mask. Questa fixture conserva la licenza MIT dell’autore; non include altri file, modelli o animazioni del tutorial. Non viene attribuita a Unity Technologies.

- [Tutorial originale dell’autore](https://diegogiacomelli.com.br/unity-avatar-mask-and-animation-layers/)
