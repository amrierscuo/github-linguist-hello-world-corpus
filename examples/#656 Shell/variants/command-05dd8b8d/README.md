# 0656: Shell: `.command`

## Latest recorded verification

**Syntax and behavior verified** for `.command`. Git for Windows sh.exe, GNU Bash invoked as POSIX sh, checks and executes the exact source. No OS file association, package manager or GUI integration is claimed. [Recorded evidence](../../verification/native_20261104_followup_2e636f6d6d616e64.json).

Textual variation of the same format, with canon suffix .command.

Origin: copy of the original `examples/#656 Shell/hello.sh` file.

Artefatto principale: `hello.command`.

Control provided, from the folder of the variant:

```text
sh -n hello.command
sh hello.command
```

Expected result: Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)
