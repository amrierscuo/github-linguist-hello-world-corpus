# 0115 Checksums: variant `.sha256sum`

Role: Manifest checksum SHA256 with real digest of the original fixture bytes; .sha2 chooses SHA-256 and .sha3 chooses SHA3 - 256 explicitly.

Type: **adapted**. Starting model: examples/#115 Checksums/SHA256SUMS; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
rhash --sha256 --check hello.sha256sum
```

Expected result: Digest of the corresponding payload; greeting.txt OK.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities](https://www.gnu.org/software/coreutils/manual/coreutils.html#sha2-utilities)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/rhash/RHash](https://github.com/rhash/RHash)
