# 0570: Python: `.wsgi`

Application WSGI conforms to the application convention; it is not a print script.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.wsgi`.

Control provided, from the folder of the variant:

```text
WSGI server: load application from hello.wsgi; local request only
```

Expected result: HTTP 200 and body Hello, World! followed by LF.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://peps.python.org/pep-3333/](https://peps.python.org/pep-3333/)
