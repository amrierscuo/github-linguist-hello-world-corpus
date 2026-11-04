# #404 M3U

Analyze an Extended M3U UTF playlist - 8 with segment title Hello, World!.

Canonical type `data`, language_id `89638692`.

Suggested toolchain: Python 3.13 and m3u8 parser.

From the example directory:

```sh
python verify.py
```

Expected result: a segment of 1s with title and URI expected; stdout greeting and LF.

example.invalid is an illustration URI: it is not downloaded or reproduced. The behavior verified is the structure and metadata of the playlist.

Recorded status: syntax verified; behavior verified. Toolchain: Python 3.13.9 + m3u8 6.0.0. [Log](verification/result.json).

Sources:

- [RFC 8216 — playlist HLS/M3U](https://www.rfc-editor.org/rfc/rfc8216)
- [m3u8 — implementazione](https://github.com/globocom/m3u8)

Install the dependencies in a separate directory:

```sh
python -m pip install m3u8==6.0.0
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m3u` | [hello.m3u](variants/m3u-333e8b48/hello.m3u) created; verification pending |
| `.m3u8` | [hello.m3u8](hello.m3u8) verified |
