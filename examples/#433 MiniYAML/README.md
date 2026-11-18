# #433 MiniYAML

## Verified on November 18, 2026

The dedicated OpenRA-style MiniYAML reader materialized the exact original file as a two-level tree. Its Greeting/Text value matched the full greeting.

Run `cargo run --quiet with the recorded reader fixture`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.yaml` | [hello.yaml](hello.yaml) Syntax and behavior verified |
| `.yml` | [hello.yml](variants/yml-ea91093d/hello.yml) created; verification pending |

</details>
