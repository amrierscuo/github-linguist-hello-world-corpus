# #068 BitBake .inc

Includes require applied to hello_1.0.bb. The original variant of the corpus retains bytes identified by checksums.

## Toolchain and verification

BitBake branch 2.10 (runtime 2.9.1), Python 3.12.3 and en_US.UTF-8. Copy the variant files into the temporary layer of the main sample. For .bbappend, BBFILES must also discover ${LAYERDIR}/*.bbappend. Use a Linux filesystem that supports Unix sockets. The main README documents the private locale.

```text
Nel layer temporaneo configurato: bitbake -p; bitbake hello -c build
```

Artifact **created**; syntax **verified**; behavior **verified**.

The original toolchain has controlled this specific variant.The BitBake task or the executable m68k produces Hello, World! and ends with exit 0. Exit does not come only from equality with the main sample.

Try: [finish_variants.json](../../verification/finish_variants.json), with commands, UTC, versions, exit code, output and hash.

## Verified Sources

- [hello.inc](hello.inc) SHA-256 `31709e6870ef89ffb69a3790ccd5c43ba96214f70b9234d0bbc2e2445b07463a`.
- [hello_1.0.bb](hello_1.0.bb) SHA-256 `2ab4132b085ecb869ec91fdbf42ece05941581dacf1911d1f09261f99ade74d3`.

## Primary sources

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10
- https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml
- https://docs.yoctoproject.org/bitbake/dev/bitbake-user-manual/bitbake-user-manual-metadata.html
