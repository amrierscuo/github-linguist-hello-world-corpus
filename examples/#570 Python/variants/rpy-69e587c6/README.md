# 0570: Python: `.rpy`

The Twisted web server .rpy resource, not a Ren’Py script.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.rpy`.

Control provided, from the folder of the variant:

```text
twistd web --path .; GET /hello.rpy from localhost
```

Expected result: HTTP body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.twisted.org/en/stable/web/howto/using-twistedweb.html](https://docs.twisted.org/en/stable/web/howto/using-twistedweb.html)
