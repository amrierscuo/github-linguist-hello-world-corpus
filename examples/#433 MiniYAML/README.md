# #433 MiniYAML

Read a MiniYaml OpenRA tree with Greeting knot and Text properties.

Canonical type `data`, language_id `4896465`.

Suggested toolchain: OpenRA MiniYaml parser original.

From the example directory:

```sh
Caricare hello.yaml con OpenRA.MiniYaml.FromFile e confrontare Greeting/Text.
```

Expected result: a Greeting node, son Text equal to Hello, World!.

MiniYaml is not standard YAML: the tab per level is provided by the format. A generic YAML parser is not counted as verification.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [OpenRA — MiniYaml](https://www.openra.net/book/modding/miniyaml/index.html)
- [OpenRA — parser originale](https://github.com/OpenRA/OpenRA/blob/bleed/OpenRA.Game/MiniYaml.cs)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.yaml` | [hello.yaml](hello.yaml) created; verification pending |
| `.yml` | [hello.yml](variants/yml-ea91093d/hello.yml) created; verification pending |
