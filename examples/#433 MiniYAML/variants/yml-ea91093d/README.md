# 0433: MiniYAML: `.yml`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#433 MiniYAML/hello.yaml.

Required toolchain: OpenRA MiniYaml parser originale. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.yml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: a Greeting node, son Text equal to Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.yml`: `a02b7e15969b17e696b80411283911ddc48042f60463ac8024881b8df9d586aa`

Primary sources:

- https://www.openra.net/book/modding/miniyaml/index.html
- https://github.com/OpenRA/OpenRA/blob/bleed/OpenRA.Game/MiniYaml.cs
