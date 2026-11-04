# 0404: M3U: `.m3u`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#404 M3U/hello.m3u8.

Required toolchain: Python 3.13.9 + m3u8 6.0.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.m3u; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: a segment of 1s with title and URI expected; stdout greeting and LF.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.m3u`: `dfcf5cbb67ed6a5acdc32e72686535b11b3d47423cc36b046cff707bd2122462`
- `verify.py`: `ee8954b2a5c23e0030ab6dcfdf09d5c57468e7777f2637e483dbd97df8f0dd9c`

Primary sources:

- https://www.rfc-editor.org/rfc/rfc8216
- https://github.com/globocom/m3u8
