# #115 Checksums

Associare al testo Hello, World! seguito da LF un manifest SHA-256 valido e verificarne l’integrità.

Tipo canonico: `data`; `language_id`: `372063053`.

Toolchain prevista: GNU Coreutils (sha256sum). La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
sha256sum --check SHA256SUMS
```

Risultato atteso: stdout `greeting.txt: OK`, uscita 0.

greeting.txt è ASCII/UTF-8 con LF. Il digest dipende dai byte: una conversione LF/CRLF cambia il checksum. Il manifest usa due spazi tra digest e nome.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: GNU Coreutils sha256sum 9.4, WSL Ubuntu 24.04. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [GNU Coreutils — verifica dei checksum](https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.crc32` | [hello.crc32](variants/ext-crc32-2e6372633332/hello.crc32) creato, verifiche pendenti |
| `.md2` | [hello.md2](variants/ext-md2-2e6d6432/hello.md2) creato, verifiche pendenti |
| `.md4` | [hello.md4](variants/ext-md4-2e6d6434/hello.md4) creato, verifiche pendenti |
| `.md5` | [hello.md5](variants/ext-md5-2e6d6435/hello.md5) creato, verifiche pendenti |
| `.sha1` | [hello.sha1](variants/ext-sha1-2e73686131/hello.sha1) creato, verifiche pendenti |
| `.sha2` | [hello.sha2](variants/ext-sha2-2e73686132/hello.sha2) creato, verifiche pendenti |
| `.sha224` | [hello.sha224](variants/ext-sha224-2e736861323234/hello.sha224) creato, verifiche pendenti |
| `.sha256` | [hello.sha256](variants/ext-sha256-2e736861323536/hello.sha256) creato, verifiche pendenti |
| `.sha256sum` | [hello.sha256sum](variants/ext-sha256sum-2e73686132353673756d/hello.sha256sum) creato, verifiche pendenti |
| `.sha3` | [hello.sha3](variants/ext-sha3-2e73686133/hello.sha3) creato, verifiche pendenti |
| `.sha384` | [hello.sha384](variants/ext-sha384-2e736861333834/hello.sha384) creato, verifiche pendenti |
| `.sha512` | [hello.sha512](variants/ext-sha512-2e736861353132/hello.sha512) creato, verifiche pendenti |
