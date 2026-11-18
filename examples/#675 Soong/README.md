# #675 Soong

## Verified on November 19, 2026

The upstream Blueprint engine loaded the original Android.bp, instantiated its module, and emitted a real Ninja build. The test host provides the subset of genrule that binds the declared out and cmd properties. Ninja ran the command and created the greeting file.

Run `go run . Android.bp && ninja -f build.ninja hello.txt && cat hello.txt`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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

</details>
