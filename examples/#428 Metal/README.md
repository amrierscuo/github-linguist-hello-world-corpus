# #428 Metal

Fill in a Metal kernel that writes the 13 bytes of greeting in a buffer.

Canonical type `programming`, language_id `230`.

Suggested toolchain: macOS Xcode Metal compiler and Metal runtime.

From the example directory:

```sh
xcrun -sdk macosx metal -c hello.metal -o build/hello.air
```

Expected result: compiled kernel; dispatch of 13 thread produces bytes ASCII Hello, World!.

The behavior also requires a Metal host with buffer and dispatch; the compilation alone is not counted as execution.

Initial state: created; syntax and behavioral verification pending. Xcode and runtime Metal not available on Windows.

Sources:

- [Apple — Metal Shading Language specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.metal` | [hello.metal](hello.metal) created; verification pending |
