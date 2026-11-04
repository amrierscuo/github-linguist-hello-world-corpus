# 0570: Python: `.fcgi`

FastCGI process via the original flick server; requires a local FastCGI frontend.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.fcgi`.

Control provided, from the folder of the variant:

```text
python hello.fcgi; frontend FastCGI local request
```

Expected result: HTTP body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.fastcgi.com/devkit/doc/fcgi-spec.html](https://www.fastcgi.com/devkit/doc/fcgi-spec.html)
- [https://pypi.org/project/flup6/](https://pypi.org/project/flup6/)
