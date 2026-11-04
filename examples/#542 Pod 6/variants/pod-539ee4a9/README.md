# 0542: Pod 6: `.pod`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#542 Pod 6/hello.pod6.

Required toolchain: Rakudo/MoarVM2022.12 originale, parser Pod6 e renderer Pod::To::Text. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.pod; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Document rendering contains Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pod`: `a0a2603939cf43362da0a40d2fbed3e79ffff948694dca57c6b341444f8ed01b`

Primary sources:

- https://docs.raku.org/language/pod
