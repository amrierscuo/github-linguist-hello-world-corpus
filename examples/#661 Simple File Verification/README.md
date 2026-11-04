# #661 Simple File Verification

The original `greeting.txt` fixture contains `Hello, World!` followed by LF.
`hello.sfv` declares his checksum CRC32 `B4E89E84`.

## Toolchain and reproduction

RHash 1.4.3, pacchetti Ubuntu amd64 `rhash` e `librhash0` 1.4.3-3build1.
The test is performed with the original packages extracted in a work directory,
without global installation, on Ubuntu 24.04 via WSL2.

From the example directory, with the real RHash available:

```sh
rhash --version
rhash -c hello.sfv
```

For an external prefix, the equivalent command is:

```sh
LD_LIBRARY_PATH=<prefisso>/usr/lib/x86_64-linux-gnu <prefisso>/usr/bin/rhash -c hello.sfv
```

Real result: `greeting.txt OK`, `Everything OK`, exit code 0.
The checker interprets the SFV file and calculates the CRC32 of the original payload.
syntax and behavior are verified for the integrity of the bytes of this fixture.
CRC32 does not certify authenticity or cryptographic security.

## Evidence

[Log nativo](verification/native.json): versione, comandi, cwd, stdout/stderr,
exit code and SHA-256 of the two original artifacts and tool packages.
La nota `path_normalization` descrive le sostituzioni dei soli percorsi locali.
No changes were made to the bytes of the payload or SFV file.
Dependencies and binaries are stored only in the work directory.

## Primary sources

- [Progetto RHash](https://github.com/rhash/RHash)
- [Manuale del progetto](https://github.com/rhash/RHash/blob/master/docs/rhash.1)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sfv` | [hello.sfv](hello.sfv) verified |
