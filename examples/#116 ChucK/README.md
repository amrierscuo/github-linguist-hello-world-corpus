# #116 ChucK

Print greetings through the ChucK diagnostic output operator.

## Reproduction

Toolchain: ChucK 1.5.2.1, silent mode. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
chuck --silent hello.ck
```

Expected result: diagnostic output containing `Hello, World!` string, any quotes and string type annotation according to the version.

## Verification

syntax and behavior verified 2026-10-08T23:32:27.751792+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://chuck.cs.princeton.edu/doc/language/overview.html](https://chuck.cs.princeton.edu/doc/language/overview.html)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.ck` | [hello.ck](hello.ck) syntax and behavior verified |
