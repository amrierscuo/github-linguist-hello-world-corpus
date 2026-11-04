# #090 CIL

Fill out a minimum SELinux CIL policy that declares hello_world_t and authorizes read on greeting_file_t; all symbols and context must be resolved.

## Toolchain

SELinux secilc 3.5-1; Ubuntu libsepol 3.5

## Commands and procedure

With secilc 3.5 on Linux, using a temporary build folder:

```sh
mkdir -p build
secilc hello.cil -o build/hello.policy -f build/file_contexts
```

The source is a minimal standalone CIL policy, with a file class, kernel SID,
user, role, types and one rule allow. The binary result demonstrates the
compilation and resolution of the model; it is not an artifact to install as
The test does not perform semodule or setenforce.

## Expected result

native exit 0 compilation and binary policy produced; no unresolved symbol or context.

## Status

syntax and behavior verified.

This canonical entry uses SELinux Common Intermediate Language (.cil), not CLR IL. The hello_world_t type represents the greeting; CIL does not print text. The check produces a temporary policy and does not load it into the system.

Actual verification of 2026-10-08T11:33:17.269986+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://github.com/SELinuxProject/selinux/tree/master/secilc/docs](https://github.com/SELinuxProject/selinux/tree/master/secilc/docs)
- [https://github.com/SELinuxProject/selinux-notebook/blob/main/src/cil_overview.md](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/cil_overview.md)
- [https://github.com/github-linguist/linguist/tree/main/samples/CIL](https://github.com/github-linguist/linguist/tree/main/samples/CIL)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cil` | [hello.cil](hello.cil) verified |
