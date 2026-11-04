# #675 Soong

Interpret a Soong Genrule module that generates a greeting file.

Canonical type `data`, language_id `222900098`.

Suggested toolchain: AOSP Soong build system.

From the example directory:

```sh
m corpus_hello_world
```

Expected result: genrule output contains Hello, World! and newline.

It is not JSON or a generic HCL: it requires the Blueprint/Soong. model

Initial state: created; syntax and behavioral verification pending. Checkout AOSP/Soong test unavailable.

Sources:

- [Soong](https://android.googlesource.com/platform/build/soong/+/refs/heads/main/README.md)
