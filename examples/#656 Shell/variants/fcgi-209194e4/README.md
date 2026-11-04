# 0656: Shell: `.fcgi`

Entrypoint shell FastCGI that initiates the original fcgiwrap adaptor; companion CGI produces header/body. Not a renamed echo.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.fcgi`.

Control provided, from the folder of the variant:

```text
spawn-fcgi -n -s /absolute/work/corpus-fcgi.sock -- sh hello.fcgi; isolated local FastCGI request SCRIPT_FILENAME=<absolute greeting.cgi>
```

Expected result: FastCGI frontend receives HTTP body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://github.com/gnosek/fcgiwrap](https://github.com/gnosek/fcgiwrap)
- [https://www.rfc-editor.org/rfc/rfc3875](https://www.rfc-editor.org/rfc/rfc3875)
