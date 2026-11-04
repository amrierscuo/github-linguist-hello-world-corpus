# #163 Debian Package Control File

Describe and extract a small native Debian source package 1.0; hello.txt extract must contain Hello, World!.

## Toolchain

Debian dpkg-source version 1.22.6.

## Commands and procedure

dpkg-source --version; dpkg-source -x hello-world-corpus_1.0.dsc build/source; cat build/source/hello.txt

## Expected result

Accepted descriptor and checksum; exit 0; hello.txt contains the newest greeting.

## Status

syntax and behavior verified.

The .dsc is a source package descriptor, with MD5, SHA - 1 and SHA-256 real of the original tar.gz included. The deterministic archive contains only hello.txt, without warnings.

Actual verification of 2026-10-08T11:56:17.956022+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://www.debian.org/doc/debian-policy/ch-controlfields.html#debian-source-control-files-dsc](https://www.debian.org/doc/debian-policy/ch-controlfields.html#debian-source-control-files-dsc)
- [https://manpages.debian.org/dpkg-dev/dpkg-source.1.en.html](https://manpages.debian.org/dpkg-dev/dpkg-source.1.en.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dsc` | [hello-world-corpus_1.0.dsc](hello-world-corpus_1.0.dsc) verified |
