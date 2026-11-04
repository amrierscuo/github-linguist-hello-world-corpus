# 0656: Shell: `.cgi`

## Latest recorded verification

**Syntax and behavior verified** for `.cgi`. Git for Windows sh.exe, GNU Bash invoked as POSIX sh, checks and executes the exact source. No OS file association, package manager or GUI integration is claimed. Check serialized CGI Content-Type header and body without starting a server. [Recorded evidence](../../verification/native_20261104_followup_2e636769.json).

CGI POSIX shell con header e body.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.cgi`.

Control provided, from the folder of the variant:

```text
sh hello.cgi
```

Expected result: header Content-Type and body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.rfc-editor.org/rfc/rfc3875](https://www.rfc-editor.org/rfc/rfc3875)
