# 0734 — Unity3D Asset — `.prefab`

Prefab Unity text serialization con GameObject/Transform originali; la stessa coppia di oggetti della scena non contiene riferimenti esterni.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.prefab`.

Controllo previsto, dalla cartella della variante:

```text
Unity Editor isolated project: import hello.prefab; inspect GameObject.name
```

Risultato atteso: GameObject chiamato Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.unity3d.com/Manual/FormatDescription.html](https://docs.unity3d.com/Manual/FormatDescription.html)
