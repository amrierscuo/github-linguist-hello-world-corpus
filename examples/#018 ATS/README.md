# #018 ATS

Write Hello World followed by a boss through main0 and println! in ATS2/Postiats.

## Reproduction

Toolchain: ATS/Postiats 0.4.2; GCC 13.3.0. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
patscc -DATS_MEMALLOC_LIBC -o hello hello.dats
./hello
Per .hats/.sats compilare ed eseguire consumer.dats dalla relativa directory variants.
```

Expected result: stdout: Hello World followed by a boss; exit 0.

## Verification

syntax and behavior verified 2026-10-08T23:32:26.148574+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html](https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html)
- [https://github.com/githwxi/ATS-Postiats](https://github.com/githwxi/ATS-Postiats)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.dats` | [hello.dats](hello.dats), [consumer.dats](variants/ext-hats-2e68617473/consumer.dats), [consumer.dats](variants/ext-sats-2e73617473/consumer.dats) syntax and behavior verified |
| `.hats` | [hello.hats](variants/ext-hats-2e68617473/hello.hats) syntax and behavior verified |
| `.sats` | [hello.sats](variants/ext-sats-2e73617473/hello.sats) syntax and behavior verified |
