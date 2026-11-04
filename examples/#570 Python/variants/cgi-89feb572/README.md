# 0570: Python: `.cgi`

## Latest recorded verification

**Syntax and behavior verified** for `.cgi`. CPython executes the exact CGI source; validates serialized Content-Type header and body, without starting a CGI server. The driver preserves the source CRLF delimiters on Windows. [Recorded evidence](../../verification/native_20261104_followup_2e636769.json).

Entrypoint CGI emitting header HTTP and greeting body.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.cgi`.

Control provided, from the folder of the variant:

```text
python hello.cgi
```

Expected result: header Content-Type and body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.rfc-editor.org/rfc/rfc3875](https://www.rfc-editor.org/rfc/rfc3875)
