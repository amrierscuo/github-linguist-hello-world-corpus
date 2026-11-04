# 0656: Shell: `.pacscript`

Original Pacstall recipe without download, dependencies or checksum invented; package writes its script in isolated pkgdir, does not install in the system.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.pacscript`.

Control provided, from the folder of the variant:

```text
bash -n hello.pacscript; Pacstall packaging-only sandbox with pkgdir under /absolute/work (no installation)
```

Expected result: test package contains original script printing Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://github.com/pacstall/pacstall/wiki/Pacscript-101](https://github.com/pacstall/pacstall/wiki/Pacscript-101)
