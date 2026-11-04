# 0205 Fancy: variant `.fancypack`

Role: Descriptor Fancy Package Specification with include_files and metadata, adapted to the original implementation of the package manager; no dependency to install.

Type: **adapted**. Starting model: examples/#205 Fancy/hello.fy; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Fancy originale: File eval: "hello.fancypack"; confrontare description e include_files della Specification; eseguire greeting.fy separatamente.
```

Expected result: Descriptor returns a Specification with Hello, World! description and includes_files greeting.fy; companion print greeting.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://github.com/bakkdoor/fancy](https://github.com/bakkdoor/fancy)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/bakkdoor/fancy/blob/master/lib/package/specification.fy](https://github.com/bakkdoor/fancy/blob/master/lib/package/specification.fy)
- [https://github.com/bakkdoor/fancy/blob/master/lib/package/dependency_installer.fy](https://github.com/bakkdoor/fancy/blob/master/lib/package/dependency_installer.fy)
