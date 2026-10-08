# #433 MiniYAML

Leggere un albero MiniYaml OpenRA con nodo Greeting e proprietà Text.

Tipo canonico `data`, language_id `4896465`.

Toolchain prevista: OpenRA MiniYaml parser originale.

Dalla cartella dell’esempio:

```sh
Caricare hello.yaml con OpenRA.MiniYaml.FromFile e confrontare Greeting/Text.
```

Risultato atteso: un nodo Greeting, figlio Text uguale a Hello, World!.

MiniYaml non è YAML standard: il tab per livello è previsto dal formato. Un parser YAML generico non viene contato come verifica.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [OpenRA — MiniYaml](https://www.openra.net/book/modding/miniyaml/index.html)
- [OpenRA — parser originale](https://github.com/OpenRA/OpenRA/blob/bleed/OpenRA.Game/MiniYaml.cs)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.yaml` | [hello.yaml](hello.yaml) creato, verifiche pendenti |
| `.yml` | [hello.yml](variants/yml-ea91093d/hello.yml) creato, verifiche pendenti |
