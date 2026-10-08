# 0734 — Unity3D Asset — `.meta`

Metadata importer Unity per TextAsset originale; il GUID è assegnato dal corpus e non riferisce asset esterni.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `greeting.asset.meta`.

Controllo previsto, dalla cartella della variante:

```text
Unity Editor isolated project: import greeting.asset together with greeting.asset.meta
```

Risultato atteso: GUID locale e userData Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.unity3d.com/Manual/AssetMetadata.html](https://docs.unity3d.com/Manual/AssetMetadata.html)
