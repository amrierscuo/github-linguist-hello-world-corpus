# #113 Chapel

Fill out a Chapel program that prints Hello, World! followed by LF.

Canonical type: `programming`; `language_id`: `55`.

Suggested toolchain: Chapel 2.x, compiler chpl. The version actually tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
chpl hello.chpl -o hello
./hello
```

Expected result: exact stdout `Hello, World!\n`, 0. output

Chapel allows a module level instruction sequence; writeln is available without explicit import.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Chapel — primo programma](https://chapel-lang.org/docs/users-guide/base/hello.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.chpl` | [hello.chpl](hello.chpl) created; verification pending |
