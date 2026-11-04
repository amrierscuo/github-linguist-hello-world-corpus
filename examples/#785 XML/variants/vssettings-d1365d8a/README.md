# 0785: XML: `.vssettings`

Fixtures of XML language for .vssettings suffix associated with Visual Studio settings. The payload is a well-format original XML; NON represents the proprietary scheme or an exportable from that application.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.vssettings`.

Control provided, from the folder of the variant:

```text
XML parser: parse hello.vssettings and assert fixture/greeting text; native application schema NOT checked
```

Expected result: a readable XML payload with the greeting Hello, World!; application compatibility is not claimed.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
