# #115 Checksums

To associate with the Hello, World! text followed by LF a SHA poster - 256 valid and verify its integrity.

Canonical type: `data`; `language_id`: `372063053`.

Suggested toolchain: GNU Coreutils (sha256sum). The version actually tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
sha256sum --check SHA256SUMS
```

Expected result: stdout `greeting.txt: OK`, 0. output

greeting.txt is ASCII/UTF-8 with LF. The digest depends on bytes: a LF/CRLF conversion changes the checksum. The poster uses two spaces between digest and name.

Recorded status: syntax verified; behavior verified. Tried toolchain: GNU Coreutils sha256sum 9.4, WSL Ubuntu 24.04. See [log](verification/verification.log).

Primary sources or original references of the project:

- [GNU Coreutils — verifica dei checksum](https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.crc32` | [hello.crc32](variants/ext-crc32-2e6372633332/hello.crc32) created; verification pending |
| `.md2` | [hello.md2](variants/ext-md2-2e6d6432/hello.md2) created; verification pending |
| `.md4` | [hello.md4](variants/ext-md4-2e6d6434/hello.md4) created; verification pending |
| `.md5` | [hello.md5](variants/ext-md5-2e6d6435/hello.md5) created; verification pending |
| `.sha1` | [hello.sha1](variants/ext-sha1-2e73686131/hello.sha1) created; verification pending |
| `.sha2` | [hello.sha2](variants/ext-sha2-2e73686132/hello.sha2) created; verification pending |
| `.sha224` | [hello.sha224](variants/ext-sha224-2e736861323234/hello.sha224) created; verification pending |
| `.sha256` | [hello.sha256](variants/ext-sha256-2e736861323536/hello.sha256) created; verification pending |
| `.sha256sum` | [hello.sha256sum](variants/ext-sha256sum-2e73686132353673756d/hello.sha256sum) created; verification pending |
| `.sha3` | [hello.sha3](variants/ext-sha3-2e73686133/hello.sha3) created; verification pending |
| `.sha384` | [hello.sha384](variants/ext-sha384-2e736861333834/hello.sha384) created; verification pending |
| `.sha512` | [hello.sha512](variants/ext-sha512-2e736861353132/hello.sha512) created; verification pending |
