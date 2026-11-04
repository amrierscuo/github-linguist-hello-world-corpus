# #068 BitBake .bbappend

The append was applied to hello_1.0.bb. The original corpus variant retains the bytes identified by the checksums.

## Toolchain and verification

BitBake branch 2.10 (runtime 2.9.1), Python 3.12.3 and en_US.UTF-8. Copy the variant files into the temporary layer of the main sample. For .bbappend, BBFILES must also discover ${LAYERDIR}/*.bbappend. Use a Linux filesystem that supports Unix sockets. The main README documents the private locale.

```text
Nel layer temporaneo configurato: bitbake -p; bitbake hello -c build
```

Artifact **created**; syntax **verified**; behavior **verified**.

The original toolchain has controlled this specific variant.The BitBake task or the executable m68k produces Hello, World! and ends with exit 0. Exit does not come only from equality with the main sample.

Try: [finish_variants.json](../../verification/finish_variants.json), with commands, UTC, versions, exit code, output and hash.

## Verified Sources

- [hello_1.0.bbappend](hello_1.0.bbappend) SHA-256 `2721f0319e22960ec2cd67c142dbec74eabf7d4018191f92bc3d8e6356f41025`.
- [hello_1.0.bb](hello_1.0.bb) SHA-256 `1496dc662a3a77b71646c974adc8847180cad1bc4b6a147cc54bd5880e7134ea`.

## Primary sources

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10
- https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml
- https://docs.yoctoproject.org/bitbake/dev/bitbake-user-manual/bitbake-user-manual-metadata.html
