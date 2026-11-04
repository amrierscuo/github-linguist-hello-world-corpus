# 0395: LiveScript: `._ls`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#395 LiveScript/hello.ls.

Required toolchain: livescript 1.6.0; Node 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello._ls; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Exit 0; Hello, World! plus newline.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello._ls`: `88f3edde83d49c7e1e3c49a41948d6e87205f4d29613b7c46eda7eaa0898b3b2`
- `package.json`: `d70b4a612ae3e0e484b2836702588994e003fb7e126add48512094e03b518222`

Primary sources:

- https://livescript.net/
- https://github.com/gkz/LiveScript
