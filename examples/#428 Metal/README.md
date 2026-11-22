# #428 Metal

## Verified on November 22, 2026

The Apple Metal compiler accepted the original shader and metallib linked it. A Swift host dispatched the greeting kernel on a Metal device, waited for completion and printed exactly `Hello, World!` from the 13-byte result buffer. The proof includes the Swift host source.

Run `xcrun -sdk macosx metal -c hello.metal -o hello.air && xcrun -sdk macosx metallib hello.air -o hello.metallib && xcrun swiftc verify.swift -o verify-metal && ./verify-metal hello.metallib`.

[Commands, toolchain, output and SHA-256](verification/native_20261122_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.metal` | [hello.metal](hello.metal) Syntax and behavior verified |

</details>
