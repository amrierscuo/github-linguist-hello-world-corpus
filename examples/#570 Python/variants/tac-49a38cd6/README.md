# 0570: Python: `.tac`

Descrittore Twisted application con endpoint limitato a loopback.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.tac`.

Control provided, from the folder of the variant:

```text
twistd --nodaemon --pidfile=work/hello.pid --logfile=work/hello.log -y hello.tac; local GET localhost:8080
```

Expected result: HTTP body Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.twisted.org/en/stable/core/howto/application.html](https://docs.twisted.org/en/stable/core/howto/application.html)
