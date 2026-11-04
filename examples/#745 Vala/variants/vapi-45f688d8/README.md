# 0745: Vala: `.vapi`

Binding Vala for an original C function; distinguished by an entrypoint Vala.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.vapi`.

Control provided, from the folder of the variant:

```text
valac --vapidir=. --pkg hello -X -I. --directory=work -o hello main.vala greeting.c; work/hello
```

Expected result: accepted binding and stdout Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://docs.vala.dev/developer-guides/bindings/writing-vapi-files.html](https://docs.vala.dev/developer-guides/bindings/writing-vapi-files.html)
