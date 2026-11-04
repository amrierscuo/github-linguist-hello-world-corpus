# 0785: XML: `.ndproj`

Fixtures of the XML language for suffix .ndproj associated with NDepend project. The payload is a well formed original XML; NON represents the proprietary scheme or an export that can be imported from that application.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.ndproj`.

Control provided, from the folder of the variant:

```text
XML parser: parse hello.ndproj and assert fixture/greeting text; native application schema NOT checked
```

Expected result: a readable XML payload with the greeting Hello, World!; application compatibility is not claimed.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
