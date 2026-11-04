# #420 Mask

Analyze Mask and make an interpolation of the target model.

Canonical type `markup`, language_id `223`.

Suggested toolchain: Node.js 22 and original MaskJS.

From the example directory:

```sh
node verify.cjs
```

Expected result: HTML <p> Hello, World! </p>; stdout greeting and LF.

The string is interpolated by the MaskJS engine; it is not replaced by a helper that imitates the format.

Recorded status: syntax verified; behavior verified. Toolchain: Node.js 22.20.0 + MaskJS 0.73.3. [Log](verification/result.json).

Sources:

- [MaskJS — motore originale](https://github.com/atmajs/MaskJS)

Fixed dependence: `npm install --ignore-scripts --no-audit --no-fund maskjs@0.73.3`. The build Node exposes render, used by the checker.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mask` | [hello.mask](hello.mask) verified |
