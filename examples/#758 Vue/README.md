# #758 Vue

Fill in a Vue Single File Component and render it server-side.

Canonical type `markup`, language_id `391`.

Suggested toolchain: Node.js22.20.0 + Vue3.5.43 compiler-sfc/server-renderer and esbuild.

From the example directory:

```sh
node verify.cjs
```

Expected result: SSR HTML exact <p> Hello, World! </p>

The declared behavior is the original SSR rendering; it does not certify events or browser interactions.

Recorded status: syntax verified; behavior verified. Toolchain: Vue3 compiler-sfc/server-renderer + esbuild original compilers. [Log](verification/result.json).

Sources:

- [Vue SFC](https://vuejs.org/api/sfc-spec.html)
- [Vue SSR](https://vuejs.org/guide/scaling-up/ssr.html)

Install the dependencies in a separate directory:

```sh
npm install vue @vue/compiler-sfc @vue/server-renderer esbuild
```

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vue` | [Hello.vue](Hello.vue) verified |
