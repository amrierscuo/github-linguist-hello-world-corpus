# #734 Unity3D Asset

Caricare una scena Unity originale con GameObject del saluto.

## Toolchain

Unity scene YAML reader/editor

## Procedura

Importare hello.unity in un progetto Unity e controllare il GameObject Hello, World! con Transform.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il goal è il nome dell’oggetto nella gerarchia, non un testo UI renderizzato; non sono inseriti GUID o script esterni.

Requisiti residui:
- Unity editor/scene loader non disponibile; compatibilità campi serializzati pending.

## Fonti primarie

- [https://docs.unity3d.com/Manual/FormatDescription.html](https://docs.unity3d.com/Manual/FormatDescription.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.anim` | [hello.anim](variants/anim-785361ae/hello.anim) creato, verifiche pendenti |
| `.asset` | [hello.asset](variants/asset-1e16658f/hello.asset) creato, verifiche pendenti |
| `.mask` | [hello.mask](variants/mask-6a9aba18/hello.mask) creato, verifiche pendenti |
| `.mat` | [hello.mat](variants/mat-6b850197/hello.mat) creato, verifiche pendenti |
| `.meta` | [greeting.asset.meta](variants/meta-e10ebe20/greeting.asset.meta) creato, verifiche pendenti |
| `.prefab` | [hello.prefab](variants/prefab-3814199a/hello.prefab) creato, verifiche pendenti |
| `.unity` | [hello.unity](hello.unity) creato, verifiche pendenti |
